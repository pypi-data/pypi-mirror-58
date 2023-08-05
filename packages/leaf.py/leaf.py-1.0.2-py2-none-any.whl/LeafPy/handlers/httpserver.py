#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys

from ..conf import settings
from ..utils.py3helpers import urlparse
from ..middleware.static import StaticMiddleware
from ..middleware.log import LogMiddleware

try:
    from http.server import HTTPServer, SimpleHTTPRequestHandler
except ImportError:
    try:
        from SimpleHTTPServer import SimpleHTTPRequestHandler
        from BaseHTTPServer import HTTPServer
    except ImportError:
        pass

__all__ = ["runsimple"]


def runbasic(func, server_address=("0.0.0.0", 8080)):
    try:
        import socketserver as SocketServer
    except ImportError:
        try:
            import SocketServer
        except ImportError:
            pass

    import socket
    import errno
    import traceback

    class WSGIHandler(SimpleHTTPRequestHandler):
        def run_wsgi_app(self):
            protocol, host, path, parameters, query, fragment = urlparse.urlparse(
                "http://dummyhost%s" % self.path
            )

            # we only use path, query
            env = {
                "wsgi.version": (1, 0),
                "wsgi.url_scheme": "http",
                "wsgi.input": self.rfile,
                "wsgi.errors": sys.stderr,
                "wsgi.multithread": 1,
                "wsgi.multiprocess": 0,
                "wsgi.run_once": 0,
                "REQUEST_METHOD": self.command,
                "REQUEST_URI": self.path,
                "PATH_INFO": path,
                "QUERY_STRING": query,
                "CONTENT_TYPE": self.headers.get("Content-Type", ""),
                "CONTENT_LENGTH": self.headers.get("Content-Length", ""),
                "REMOTE_ADDR": self.client_address[0],
                "SERVER_NAME": self.server.server_address[0],
                "SERVER_PORT": str(self.server.server_address[1]),
                "SERVER_PROTOCOL": self.request_version,
            }

            for http_header, http_value in self.headers.items():
                env["HTTP_%s" % http_header.replace("-", "_").upper()] = http_value

            # Setup the state
            self.wsgi_sent_headers = 0
            self.wsgi_headers = []

            try:
                # We have there environment, now invoke the application
                result = self.server.app(env, self.wsgi_start_response)
                try:
                    try:
                        for data in result:
                            if data:
                                self.wsgi_write_data(data)
                    finally:
                        if hasattr(result, "close"):
                            result.close()
                except socket.error as socket_err:
                    # Catch common network errors and suppress them
                    if socket_err.args[0] in (errno.ECONNABORTED, errno.EPIPE):
                        return
                except socket.timeout:
                    return
            except:
                print(traceback.format_exc(), file=settings.DEBUG)

            if not self.wsgi_sent_headers:
                # We must write out something!
                self.wsgi_write_data(" ")
            return

        do_POST = run_wsgi_app
        do_PUT = run_wsgi_app
        do_DELETE = run_wsgi_app

        def do_GET(self):
            if self.path.startswith("/static/"):
                SimpleHTTPRequestHandler.do_GET(self)
            else:
                self.run_wsgi_app()

        def wsgi_start_response(self, response_status, response_headers, exc_info=None):
            if self.wsgi_sent_headers:
                raise Exception("Headers already sent and start_response called again!")
            # Should really take a copy to avoid changes in the application....
            self.wsgi_headers = (response_status, response_headers)
            return self.wsgi_write_data

        def wsgi_write_data(self, data):
            if not self.wsgi_sent_headers:
                status, headers = self.wsgi_headers
                # Need to send header prior to data
                status_code = status[: status.find(" ")]
                status_msg = status[status.find(" ") + 1:]
                self.send_response(int(status_code), status_msg)
                for header, value in headers:
                    self.send_header(header, value)
                self.end_headers()
                self.wsgi_sent_headers = 1
            # Send the data
            self.wfile.write(data)

    class WSGIServer(SocketServer.ThreadingMixIn, HTTPServer):
        def __init__(self, func, server_address):
            HTTPServer.HTTPServer.__init__(self, server_address, WSGIHandler)
            self.app = func
            self.serverShuttingDown = 0

    print("http://%s:%d/" % server_address)
    WSGIServer(func, server_address).serve_forever()


# The WSGIServer instance.
# Made global so that it can be stopped in embedded mode.
server = None


def runsimple(func, server_address=("0.0.0.0", 8080)):
    """
    Runs [CherryPy][cp] WSGI server hosting WSGI app `func`.
    The directory `static/` is hosted statically.

    [cp]: http://www.cherrypy.org
    """
    global server
    func = StaticMiddleware(func)
    func = LogMiddleware(func)

    server = WSGIServer(server_address, func)

    if "/" in server_address[0]:
        print("%s" % server_address)
    else:
        if server.ssl_adapter:
            print("https://%s:%d/" % server_address)
        else:
            print("http://%s:%d/" % server_address)

    try:
        server.start()
    except (KeyboardInterrupt, SystemExit):
        server.stop()
        server = None


def WSGIServer(server_address, wsgi_app):
    """Creates CherryPy WSGI server listening at `server_address` to serve `wsgi_app`.
    This function can be overwritten to customize the webserver or use a different webserver.
    """
    from cheroot import wsgi

    server = wsgi.Server(server_address, wsgi_app, server_name="localhost")
    server.nodelay = not sys.platform.startswith(
        "java"
    )  # TCP_NODELAY isn't supported on the JVM
    return server
