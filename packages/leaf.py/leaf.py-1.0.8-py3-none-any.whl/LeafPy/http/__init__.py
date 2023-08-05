#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = [
    "textresult", "jsonresult",
    "HTTPError",
    "Redirect", "redirect",
    "SeeOther", "seeother",
    "NotFound", "notfound",
    "NoMethod", "nomethod",
    "InternalError", "internalerror",
    "BadRequest", "badrequest",
    "header", "data", "rawinput", "input",
    "request", "Request",
    "session", "setcookie", "decode_cookie", "parse_cookies", "cookies",
    "render", "TemplateResponse"
]

import cgi

from ..template import frender
from ..utils import dictadd, intget
from ..utils.datastructs import (
    threadeddict,
    storage,
    storify,
)
from ..utils.encoding import safestr
from ..utils.py3helpers import (
    PY2,
    urljoin,
    BytesIO,
    text_type,
    quote,
    unquote,
)

from .resultstruct import (
    textresult,
    jsonresult
)

if PY2:
    from Cookie import (
        CookieError,
        Morsel,
        SimpleCookie
    )
else:
    from http.cookies import (
        CookieError,
        Morsel,
        SimpleCookie
    )

render = None
session = None


class HTTPError(Exception):
    def __init__(self, status, headers={}, data=""):
        request.status = status
        for k, v in headers.items():
            header(k, v)
        self.data = data
        Exception.__init__(self, status)


class Redirect(HTTPError):
    """A `301 Moved Permanently` redirect."""

    def __init__(self, url, status="301 Moved Permanently", absolute=False):
        """
        Returns a `status` redirect to the new URL.
        `url` is joined with the base URL so that things like
        `redirect("about") will work properly.
        """
        newloc = urljoin(request.path, url)

        if newloc.startswith("/"):
            if absolute:
                home = request.realhome
            else:
                home = request.home
            newloc = home + newloc

        headers = {"Content-Type": "text/html", "Location": newloc}
        HTTPError.__init__(self, status, headers, "")


redirect = Redirect


class SeeOther(Redirect):
    """A `303 See Other` redirect."""

    def __init__(self, url, absolute=False):
        Redirect.__init__(self, url, "303 See Other", absolute=absolute)


seeother = SeeOther


class _NotFound(HTTPError):
    """`404 Not Found` error."""

    message = "not found"

    def __init__(self, message=None):
        status = "404 Not Found"
        headers = {"Content-Type": "text/html; charset=utf-8"}
        HTTPError.__init__(self, status, headers, message or self.message)


def NotFound(message=None):
    """Returns HTTPError with '404 Not Found' error from the active application.
    """
    if message:
        return _NotFound(message)
    elif request.get("app_stack"):
        return request.app_stack[-1].notfound()
    else:
        return _NotFound()


notfound = NotFound


class NoMethod(HTTPError):
    """A `405 Method Not Allowed` error."""

    message = "method not allowed"

    def __init__(self, cls=None):
        status = "405 Method Not Allowed"
        headers = {}
        headers["Content-Type"] = "text/html"

        methods = ["GET", "HEAD", "POST", "PUT", "DELETE"]
        if cls:
            methods = [method for method in methods if hasattr(cls, method)]

        headers["Allow"] = ", ".join(methods)
        HTTPError.__init__(self, status, headers, self.message)


nomethod = NoMethod


class _InternalError(HTTPError):
    """500 Internal Server Error`."""

    message = "internal server error"

    def __init__(self, message=None):
        status = "500 Internal Server Error"
        headers = {"Content-Type": "text/html"}
        HTTPError.__init__(self, status, headers, message or self.message)


def InternalError(message=None):
    """Returns HTTPError with '500 internal error' error from the active application.
    """
    if message:
        return _InternalError(message)
    elif request.get("app_stack"):
        return request.app_stack[-1].internalerror()
    else:
        return _InternalError()


internalerror = InternalError


class BadRequest(HTTPError):
    """`400 Bad Request` error."""

    message = "bad request"

    def __init__(self, message=None):
        status = "400 Bad Request"
        headers = {"Content-Type": "text/html"}
        HTTPError.__init__(self, status, headers, message or self.message)


badrequest = BadRequest


def header(hdr, value, unique=False):
    hdr, value = safestr(hdr), safestr(value)
    if "\n" in hdr or "\r" in hdr or "\n" in value or "\r" in value:
        raise ValueError("invalid characters in header")
    if unique is True:
        for h, v in request.headers:
            if h.lower() == hdr.lower():
                return

    request.headers.append((hdr, value))


def data():
    if 'data' not in request:
        cl = intget(request.env.get('CONTENT_LENGTH'), 0)
        request.data = request.env['wsgi.input'].read(cl)
    return request.data


def rawinput(method=None):
    """Returns storage object with GET or POST arguments.
    """
    method = method or "both"
    from ..utils.py3helpers import StringIO

    def dictify(fs):
        if fs.list is None: fs.list = []
        return dict([(k, fs[k]) for k in fs.keys()])

    e = request.env.copy()
    a = b = {}

    if method.lower() in ['both', 'post', 'put']:
        if e['REQUEST_METHOD'] in ['POST', 'PUT']:
            if e.get('CONTENT_TYPE', '').lower().startswith('multipart/'):
                a = request.get('_fieldstorage')
                if not a:
                    fp = e['wsgi.input']
                    a = cgi.FieldStorage(fp=fp, environ=e, keep_blank_values=1)
                    request._fieldstorage = a
            else:
                fp = BytesIO(data())
                a = cgi.FieldStorage(fp=fp, environ=e, keep_blank_values=1)
            a = dictify(a)

    if method.lower() in ['both', 'get']:
        e['REQUEST_METHOD'] = 'GET'
        b = dictify(cgi.FieldStorage(environ=e, keep_blank_values=1))

    def process_fieldstorage(fs):
        if isinstance(fs, list):
            return [process_fieldstorage(x) for x in fs]
        elif fs.filename is None:
            return fs.value
        else:
            return fs

    return storage([(k, process_fieldstorage(v)) for k, v in dictadd(b, a).items()])


def input(*requireds, **defaults):
    _method = defaults.pop('_method', 'both')
    out = rawinput(_method)
    try:
        defaults.setdefault('_unicode', True)  # force unicode conversion by default.
        return storify(out, *requireds, **defaults)
    except KeyError:
        raise badrequest()


request = Request = threadeddict()
request.__doc__ = """
for webapps request args
"""


def setcookie(name, value, expires="", domain=None, secure=False, httponly=False, path=None, samesite=None):
    """Sets a cookie."""
    morsel = Morsel()
    name, value = safestr(name), safestr(value)
    morsel.set(name, value, quote(value))
    if isinstance(expires, int) and expires < 0:
        expires = -1000000000
    morsel["expires"] = expires
    morsel["path"] = path or request.homepath + "/"
    if domain:
        morsel["domain"] = domain
    if secure:
        morsel["secure"] = secure
    if httponly:
        morsel["httponly"] = True
    value = morsel.OutputString()
    if samesite and samesite.lower() in ("strict", "lax"):
        value += "; SameSite=%s" % samesite
    header("Set-Cookie", value)


def decode_cookie(value):
    r"""Safely decodes a cookie value to unicode.

    Tries us-ascii, utf-8 and io8859 encodings, in that order.

    > decode_cookie('')
    u''
    > decode_cookie('asdf')
    u'asdf'
    > decode_cookie('foo \xC3\xA9 bar')
    u'foo \xe9 bar'
    > decode_cookie('foo \xE9 bar')
    u'foo \xe9 bar'
    """
    try:
        # First try plain ASCII encoding
        return text_type(value, "us-ascii")
    except UnicodeError:
        # Then try UTF-8, and if that fails, ISO8859
        try:
            return text_type(value, "utf-8")
        except UnicodeError:
            return text_type(value, "iso8859", "ignore")
        except TypeError:
            return text_type(value)
    except TypeError:
        return text_type(value)


def parse_cookies(http_cookie):
    r"""Parse a HTTP_COOKIE header and return dict of cookie names and decoded values.
    > sorted(parse_cookies('').items())
    []
    > sorted(parse_cookies('a=1').items())
    [('a', '1')]
    > sorted(parse_cookies('a=1%202').items())
    [('a', '1 2')]
    > sorted(parse_cookies('a=Z%C3%A9Z').items())
    [('a', 'Z\xc3\xa9Z')]
    > sorted(parse_cookies('a=1; b=2; c=3').items())
    [('a', '1'), ('b', '2'), ('c', '3')]

    # > sorted(parse_cookies('a=1; b=w("x")|y=z; c=3').items())
    # [('a', '1'), ('b', 'w('), ('c', '3')]

    > sorted(parse_cookies('a=1; b=w(%22x%22)|y=z; c=3').items())
    [('a', '1'), ('b', 'w("x")|y=z'), ('c', '3')]

    > sorted(parse_cookies('keebler=E=mc2').items())
    [('keebler', 'E=mc2')]
    > sorted(parse_cookies(r'keebler="E=mc2; L=\"Loves\"; fudge=\012;"').items())
    [('keebler', 'E=mc2; L="Loves"; fudge=\n;')]
    """
    if '"' in http_cookie:
        cookie = SimpleCookie()
        try:
            cookie.load(http_cookie)
        except CookieError:
            cookie = SimpleCookie()
            for attr_value in http_cookie.split(";"):
                try:
                    cookie.load(attr_value)
                except CookieError:
                    pass
        cookies = dict([(k, unquote(v.value)) for k, v in cookie.items()])
    else:
        cookies = {}
        for key_value in http_cookie.split(";"):
            key_value = key_value.split("=", 1)
            if len(key_value) == 2:
                key, value = key_value
                cookies[key.strip()] = unquote(value.strip())
    return cookies


def cookies(*requireds, **defaults):
    """Returns a `storage` object with all the request cookies in it.
    See `storify` for how `requireds` and `defaults` work.

    This is forgiving on bad HTTP_COOKIE input, it tries to parse at least
    the cookies it can.

    The values are converted to unicode if _unicode=True is passed.
    """
    # If _unicode=True is specified, use decode_cookie to convert cookie value to unicode
    if defaults.get("_unicode") is True:
        defaults["_unicode"] = decode_cookie

    # parse cookie string and cache the result for next time.
    if "_parsed_cookies" not in request:
        http_cookie = request.env.get("HTTP_COOKIE", "")
        request._parsed_cookies = parse_cookies(http_cookie)

    try:
        return storify(request._parsed_cookies, *requireds, **defaults)
    except KeyError:
        badrequest()
        raise StopIteration()


def TemplateResponse(filename, mime_type=None, args=None, **kwargs):
    args = args or {}
    assert isinstance(args, dict) == True

    kwargs = dict(kwargs, **args)
    template_file = filename or kwargs.pop("template_file", None)
    content_type = mime_type or kwargs.pop("mime_type", None)
    if not filename:
        assert KeyError("template_file can't empty")

    _template = frender(template_file)
    if content_type:
        return _template(content_type, **kwargs)
    return _template(**kwargs)
