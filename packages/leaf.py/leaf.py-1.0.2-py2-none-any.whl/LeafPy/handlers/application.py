#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import traceback
import itertools
import wsgiref
from inspect import isclass, isfunction

from . import wsgi, httpserver, session
from .. import http, utils, template
from ..http import debugerror
from ..conf import settings
from ..utils.py3helpers import is_iter, string_types, PY2, iteritems, unquote
from ..utils import datastructs, lstrips, importlib

try:
    from importlib import reload  # Since Py 3.4 reload is in importlib
except ImportError:
    try:
        from imp import reload  # Since Py 3.0 and before 3.4 reload is in imp
    except ImportError:
        pass  # Before Py 3.0 reload is a global function


class application:
    def __init__(self, fvars={}, autoreload=None):
        settings.configure(fvars)

        if not autoreload:
            autoreload = settings.DEBUG

        self._init_mapping()
        self.fvars = fvars
        self.processors = []
        self.deploy_path = settings.DEPLOY_PATH.strip()

        self.add_processor(loadhook(self._load))
        self.add_processor(unloadhook(self._unload))

        http.session = session.Session(self)
        http.render = template.get_render()

        if autoreload:
            def reload_settings():
                settings.configure(self.fvars)

            def reload_mapping():
                self._init_mapping()

            def reload_render():
                http.render = template.get_render()

            self.add_processor(loadhook(Reloader()))
            self.add_processor(loadhook(reload_settings))
            self.add_processor(loadhook(reload_mapping))
            self.add_processor(loadhook(reload_render))

    def _load(self):
        http.request.app_stack.append(self)

    def _unload(self):
        http.request.app_stack = http.request.app_stack[:-1]
        if http.request.app_stack:
            oldrequest = http.request.get("_oldrequest")
            if oldrequest:
                http.request.home = oldrequest.home
                http.request.homepath = oldrequest.homepath
                http.request.path = oldrequest.path
                http.request.fullpath = oldrequest.fullpath

    def _cleanup(self):
        datastructs.ThreadedDict.clear_all()

    def _init_mapping(self):
        mod = importlib.import_module(".urls", settings.APP_NAME)
        if hasattr(mod, "urlpatterns"):
            mapping = mod.urlpatterns
        else:
            mapping = ()
        if type(mapping) is dict:
            mapping = list(sum(mapping.items(), ()))
        self.mapping = list(utils.group(mapping, 2))

    def add_mapping(self, pattern, classname):
        self.mapping.append((pattern, classname))

    def add_processor(self, processor):
        self.processors.append(processor)

    def handle(self):
        fn, args = self._match(self.mapping, http.request.path)
        return self._delegate(fn, self.fvars, args)

    def handle_with_processors(self):
        def process(processors):
            try:
                if processors:
                    p, processors = processors[0], processors[1:]
                    return p(lambda: process(processors))
                else:
                    return self.handle()
            except http.HTTPError:
                raise
            except (KeyboardInterrupt, SystemExit):
                raise
            except:
                print(traceback.format_exc())
                raise self.internalerror()

        # processors must be applied in the resvere order. (??)
        return process(self.processors)

    def wsgifunc(self, *middleware):
        def peep(iterator):
            try:
                firstchunk = next(iterator)
            except StopIteration:
                firstchunk = ""

            return itertools.chain([firstchunk], iterator)

        def wsgi(env, start_resp):
            self._cleanup()
            self.load(env)

            try:
                if http.request.method.upper() != http.request.method:
                    raise http.nomethod()

                result = self.handle_with_processors()
                if isinstance(result, tuple) and len(result) == 2:
                    content_type, result = result[:2]
                    http.header("Content-type", content_type, unique=True)
                elif is_iter(result):
                    result = peep(result)
                else:
                    result = [result]
            except http.HTTPError as e:
                result = [e.data]

            def build_result(result):
                for r in result:
                    if PY2:
                        yield utils.safestr(r)
                    else:
                        if isinstance(r, bytes):
                            yield r
                        elif isinstance(r, string_types):
                            yield r.encode("utf-8")
                        else:
                            yield str(r).encode("utf-8")

            result = build_result(result)

            status, headers = http.request.status, http.request.headers
            start_resp(status, headers)

            def cleanup():
                self._cleanup()
                yield b""  # force this function to be a generator

            return itertools.chain(result, cleanup())

        for m in middleware:
            wsgi = m(wsgi)

        return wsgi

    def run(self, *middleware):
        return wsgi.runwsgi(self.wsgifunc(*middleware))

    def stop(self):
        if httpserver.server:
            httpserver.server.stop()
            httpserver.server = None

    def cgirun(self, *middleware):
        wsgiapp = self.wsgifunc(*middleware)
        try:
            from google.appengine.ext.webapp.util import run_wsgi_app
            return run_wsgi_app(wsgiapp)
        except ImportError:
            return wsgiref.handlers.CGIHandler().run(wsgiapp)

    def gaerun(self, *middleware):
        wsgiapp = self.wsgifunc(*middleware)
        try:
            # check what version of python is running
            version = sys.version_info[:2]
            major = version[0]
            minor = version[1]

            if major != 2:
                raise EnvironmentError(
                    "Google App Engine only supports python 2.5 and 2.7"
                )

            # if 2.7, return a function that can be run by gae
            if minor == 7:
                return wsgiapp
            # if 2.5, use run_wsgi_app
            elif minor == 5:
                from google.appengine.ext.webapp.util import run_wsgi_app

                return run_wsgi_app(wsgiapp)
            else:
                raise EnvironmentError(
                    "Not a supported platform, use python 2.5 or 2.7"
                )
        except ImportError:
            return wsgiref.handlers.CGIHandler().run(wsgiapp)

    def load(self, env):
        """Initializes request using env."""
        request = http.request
        request.clear()
        request.status = "200 OK"
        request.headers = []
        request.output = ""
        request.environ = request.env = env
        request.host = env.get("HTTP_HOST")

        if env.get("wsgi.url_scheme") in ["http", "https"]:
            request.protocol = env["wsgi.url_scheme"]
        elif env.get("HTTPS", "").lower() in ["on", "true", "1"]:
            request.protocol = "https"
        else:
            request.protocol = "http"
        request.homedomain = request.protocol + "://" + env.get("HTTP_HOST", "[unknown]")
        request.homepath = os.environ.get("REAL_SCRIPT_NAME", env.get("SCRIPT_NAME", ""))
        request.home = request.homedomain + request.homepath
        request.realhome = request.home
        request.ip = env.get("REMOTE_ADDR")
        request.method = env.get("REQUEST_METHOD")
        if PY2:
            request.path = env.get("PATH_INFO")
        else:
            request.path = env.get("PATH_INFO").encode("latin1").decode("utf8")
        if env.get("SERVER_SOFTWARE", "").startswith("lighttpd/"):
            request.path = lstrips(env.get("REQUEST_URI").split("?")[0], request.homepath)
            request.path = unquote(request.path)

        if env.get("QUERY_STRING"):
            request.query = "?" + env.get("QUERY_STRING", "")
        else:
            request.query = ""

        request.fullpath = request.path + request.query

        for k, v in iteritems(request):
            if isinstance(v, bytes):
                request[k] = v.decode("utf-8", "replace")

        request.status = "200 OK"
        request.app_stack = []

    def _match(self, mapping, value):
        for pat, what in mapping:
            if isinstance(what, application):
                if value.startswith(pat):
                    f = lambda: self._delegate_sub_application(pat, what)
                    return f, None
                else:
                    continue
            elif isinstance(what, string_types):
                what, result = utils.re_subm(r"^%s\Z" % (pat,), what, value)
            else:
                result = utils.re_compile(r"^%s\Z" % (pat,)).match(value)

            if result:  # it's a match
                return what, [x for x in result.groups()]
        return None, None

    def _delegate(self, f, fvars, args=[]):
        def handle_class(cls):
            meth = http.request.method
            if meth == "HEAD" and not hasattr(cls, meth):
                meth = "GET"
            if not hasattr(cls, meth):
                raise http.nomethod(cls)
            tocall = getattr(cls(), meth)
            return tocall(*args)

        def handle_function(tocall):
            c = tocall.__code__.co_argcount
            if (c - len(args)) > 0:
                return tocall(http.request, *args)
            else:
                return tocall(*args)

        def handle_object(o):
            if isfunction(o):
                return handle_function(o)
            if isclass(o):
                return handle_class(o)
            return http._InternalError("Not Support Object Type:%s" % type(o))

        if f is None:
            raise http.notfound()
        elif isinstance(f, application):
            return f.handle_with_processors()
        elif isfunction(f):
            return handle_function(f)
        elif isclass(f):
            return handle_class(f)
        elif isinstance(f, string_types):
            if f.startswith("redirect "):
                url = f.split(" ", 1)[1]
                if http.request.method == "GET":
                    x = http.request.env.get("QUERY_STRING", "")
                    if x:
                        url += "?" + x
                raise http.redirect(url)
            elif "." in f:
                mod, cls = f.rsplit(".", 1)
                mod = importlib.import_module(mod, settings.APP_NAME)
                if not settings.DEBUG:
                    try:
                        reload(mod)
                    except ImportError:
                        pass
                cls = getattr(mod, cls)
            else:
                cls = fvars[f]
            return handle_object(cls)
        elif hasattr(f, "__call__"):
            return f()
        else:
            return http.notfound()

    def _delegate_sub_application(self, dir, app):
        http.request._oldrequest = datastructs.storage(http.request)
        http.request.home += dir
        http.request.homepath += dir
        http.request.path = http.request.path[len(dir):]
        http.request.fullpath = http.request.fullpath[len(dir):]
        return app.handle_with_processors()

    def get_parent_app(self):
        if self in http.request.app_stack:
            index = http.request.app_stack.index(self)
            if index > 0:
                return http.request.app_stack[index - 1]

    def notfound(self):
        parent = self.get_parent_app()
        if parent:
            return parent.notfound()
        else:
            return http._NotFound()

    def internalerror(self):
        parent = self.get_parent_app()
        if parent:
            return parent.internalerror()
        elif settings.DEBUG:
            # return http._InternalError("Debug Error 500")
            return debugerror.debugerror()
        else:
            return http._InternalError()


def loadhook(h):
    def processor(handler):
        h()
        return handler()

    return processor


def unloadhook(h):
    def processor(handler):
        try:
            result = handler()
            is_gen = is_iter(result)
        except:
            # run the hook even when handler raises some exception
            h()
            raise

        if is_gen:
            return wrap(result)
        else:
            h()
            return result

    def wrap(result):
        def next_hook():
            try:
                return next(result)
            except:
                # call the hook at the and of iterator
                h()
                raise

        result = iter(result)
        while True:
            try:
                yield next_hook()
            except StopIteration:
                return

    return processor


def autodelegate(prefix=''):
    def internal(self, *arg):
        if len(arg) > 0:
            fixact, args = arg[0], list(arg[1:])
        else:
            fixact, args = "", []

        if '/' in fixact:
            first, rest = fixact.split('/', 1)
            func = prefix + first
            args.insert(0, '/' + rest)
        else:
            func = prefix + fixact

        if hasattr(self, func):
            try:
                return getattr(self, func)(*args)
            except TypeError:
                raise http.notfound()
        else:
            raise http.notfound()

    return internal


class Reloader:
    if sys.platform.startswith("java"):
        SUFFIX = "$py.class"
    else:
        SUFFIX = ".pyc"

    def __init__(self):
        self.mtimes = {}

    def __call__(self):
        for mod in list(sys.modules.values()):
            self.check(mod)

    def check(self, mod):
        if not (mod and hasattr(mod, "__file__") and mod.__file__):
            return

        try:
            mtime = os.stat(mod.__file__).st_mtime
        except (OSError, IOError):
            return
        if mod.__file__.endswith(self.__class__.SUFFIX) and os.path.exists(mod.__file__[:-1]):
            mtime = max(os.stat(mod.__file__[:-1]).st_mtime, mtime)

        if mod not in self.mtimes:
            self.mtimes[mod] = mtime
        elif self.mtimes[mod] < mtime:
            try:
                reload(mod)
                self.mtimes[mod] = mtime
            except ImportError:
                pass
