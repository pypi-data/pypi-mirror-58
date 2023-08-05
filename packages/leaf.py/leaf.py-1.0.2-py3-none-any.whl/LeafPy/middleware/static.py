#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import os
import posixpath
from ..conf import settings
from ..utils.py3helpers import BytesIO, unquote

try:
    from http.server import SimpleHTTPRequestHandler
except ImportError:
    try:
        from SimpleHTTPServer import SimpleHTTPRequestHandler
    except ImportError:
        pass


class StaticApp(SimpleHTTPRequestHandler):
    """WSGI application for serving static files."""

    def __init__(self, environ, start_response):
        self.headers = []
        self.environ = environ
        self.start_response = start_response
        self.directory = os.getcwd()

    def send_response(self, status, msg=""):
        # the int(status) call is needed because in Py3 status is an enum.IntEnum and we need the integer behind
        self.status = str(int(status)) + " " + msg

    def send_header(self, name, value):
        self.headers.append((name, value))

    def end_headers(self):
        pass

    def log_message(*a):
        pass

    def __iter__(self):
        environ = self.environ

        self.path = environ.get("PATH_INFO", "")
        self.client_address = (
            environ.get("REMOTE_ADDR", "-"),
            environ.get("REMOTE_PORT", "-"),
        )
        self.command = environ.get("REQUEST_METHOD", "-")

        self.wfile = BytesIO()  # for capturing error

        try:
            path = self.translate_path(self.path)
            etag = '"%s"' % os.path.getmtime(path)
            client_etag = environ.get("HTTP_IF_NONE_MATCH")
            self.send_header("ETag", etag)
            if etag == client_etag:
                self.send_response(304, "Not Modified")
                self.start_response(self.status, self.headers)
                raise StopIteration()
        except OSError:
            pass  # Probably a 404

        f = self.send_head()
        self.start_response(self.status, self.headers)

        if f:
            block_size = 16 * 1024
            while True:
                buf = f.read(block_size)
                if not buf:
                    break
                yield buf
            f.close()
        else:
            value = self.wfile.getvalue()
            yield value


class StaticMiddleware:
    """WSGI middleware for serving static files."""

    def __init__(self, app):
        self.app = app
        self.prefix = None

    def _gen_prefix(self):
        _prefix = list(settings.STATIC_DIRS)
        _prefix.extend(settings.STATIC_PATH)
        return tuple(set(_prefix))

    def __call__(self, environ, start_response):
        path = environ.get("PATH_INFO", "")
        path = self.normpath(path)

        if self.is_static(path):
            return StaticApp(environ, start_response)
        else:
            return self.app(environ, start_response)

    def is_static(self, path):
        if not self.prefix:
            self.prefix = self._gen_prefix()

        for p in self.prefix:
            if path.startswith(p):
                return True
        return False

    def normpath(self, path):
        path2 = posixpath.normpath(unquote(path))
        if path.endswith("/"):
            path2 += "/"
        return path2
