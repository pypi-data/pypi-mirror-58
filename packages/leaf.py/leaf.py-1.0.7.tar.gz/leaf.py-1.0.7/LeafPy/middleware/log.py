#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
from ..utils import safestr
from ..utils.py3helpers import BytesIO

try:
    from http.server import BaseHTTPRequestHandler
except ImportError:
    try:
        from BaseHTTPServer import BaseHTTPRequestHandler
    except ImportError:
        pass


class LogMiddleware:
    """WSGI middleware for logging the status."""

    def __init__(self, app):
        self.app = app
        self.format = '%s - - [%s] "%s %s %s" - %s'

        f = BytesIO()

        class FakeSocket:
            def makefile(self, *a):
                return f

        # take log_date_time_string method from BaseHTTPRequestHandler
        self.log_date_time_string = BaseHTTPRequestHandler(
            FakeSocket(), None, None
        ).log_date_time_string

    def __call__(self, environ, start_response):
        def xstart_response(status, response_headers, *args):
            out = start_response(status, response_headers, *args)
            self.log(status, environ)
            return out

        return self.app(environ, xstart_response)

    def log(self, status, environ):
        outfile = environ.get("wsgi.errors", sys.stderr)
        req = environ.get("PATH_INFO", "_")
        protocol = environ.get("ACTUAL_SERVER_PROTOCOL", "-")
        method = environ.get("REQUEST_METHOD", "-")
        host = "%s:%s" % (
            environ.get("REMOTE_ADDR", "-"),
            environ.get("REMOTE_PORT", "-"),
        )

        time = self.log_date_time_string()

        msg = self.format % (host, time, protocol, method, req, status)
        print(safestr(msg), file=outfile)
