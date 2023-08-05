#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from ..conf import settings
from ..utils import encoding, net

from ._compiler import Compiler
from ..utils.py3helpers import (
    PY2,
    text_type,
    BytesIO,
    escape as htmlescape,
)


class IncludePageError(Exception):
    pass


class Out(object):
    def __init__(self, template):
        self._template = template
        self._buf = BytesIO()
        self._encoding = settings.DEFAULT_CHARSET

    def _str(self, text):
        if text is None:
            return ""
        elif isinstance(text, text_type):
            return text.encode(self._encoding)
        elif isinstance(text, str):
            return encoding.safeunicode(text).encode(self._encoding)
        else:
            return str(text)

    def write(self, *args, **kwargs):
        text = " ".join(args)
        besc = kwargs.get("escape", True)
        s = self._str(text)
        if besc:
            if PY2:
                self._buf.write(htmlescape(s))
            else:
                self._buf.write(htmlescape(s.decode()).encode())
        else:
            self._buf.write(s)

    def escape(self, txt):
        return net.websafe(txt)

    def str2hex(self, txt, slen=0):
        return encoding.str2hex(txt, slen)

    def safeutf8(self, txt, slen=0):
        return encoding.safeutf8(txt, slen)

    def include(self, path, *args, **kwargs):
        escape = kwargs.pop("escape", False)
        path = os.path.join(os.path.dirname(os.path.abspath(self._template.filename)), path)
        _template = Template(open(path).read(), filename=path, \
                             env=self._template.env, fvars=self._template.fvars)
        self.write(_template(*args, **kwargs), escape=escape)

    def getvalue(self):
        return self._buf.getvalue()


class Template:
    CONTENT_TYPES = {
        '.html': 'text/html; charset=utf-8',
        '.xhtml': 'application/xhtml+xml; charset=utf-8',
        '.txt': 'text/plain;charset=utf-8',
        '.json': 'application/json;charset=utf-8',
        '.xml': 'application/xml;charset=utf-8',
    }
    fvars = {}
    env = {}

    def __init__(self, text, filename='<template>', env=None, fvars=None):
        self._compile_class = Compiler(not settings.DEBUG)
        self.filename = filename

        if isinstance(env, dict):
            self.env = dict(self.env, **env)
        if isinstance(fvars, dict):
            self.fvars = dict(self.fvars, **fvars)

        self.source_code = self._load_source(text)

        _, ext = os.path.splitext(filename)
        self.content_type = self.CONTENT_TYPES.get(ext, settings.DEF_CONTENT_TYPES)

    def _load_source(self, text):
        text = Template.normalize_text(text)
        return self._compile_class(text)

    def normalize_text(text):
        """Normalizes template text by correcting \r\n, tabs and BOM chars."""
        text = text.replace('\r\n', '\n').replace('\r', '\n').expandtabs()
        if not text.endswith('\n'):
            text += '\n'

        # ignore BOM chars at the begining of template
        BOM = '\xef\xbb\xbf'
        if isinstance(text, str) and text.startswith(BOM):
            text = text[len(BOM):]

        return text

    normalize_text = staticmethod(normalize_text)

    def _f(self, env, fvars):
        def defined(v):
            return (v in env) or (v in fvars)

        return defined

    def _unf(self, env, fvars):
        def undefined(v):
            return not ((v in env) or (v in fvars))

        return undefined

    def _pathinfo(self):
        _path = None
        if hasattr(settings, "DEPLOY_PATH"):
            _path = settings.DEPLOY_PATH
        if not _path:
            _path = "./"
        if _path.endswith("/"):
            return _path
        return "%s/" % _path

    contextPath = property(_pathinfo)

    def make_env(self, out, *args, **kwargs):
        env = dict(self.env, **kwargs)
        return dict(env,
                    out=out,
                    str2hex=out.str2hex,
                    safeutf8=out.safeutf8,
                    utf8=out.safeutf8,
                    include=out.include,
                    escape=out.escape,
                    defined=self._f(self.env, self.fvars),
                    undefined=self._unf(self.env, self.fvars),
                    contextPath=self.contextPath
                    )

    def __call__(self, *args, **kwargs):
        out = Out(self)

        args = args[:2]
        if len(args) == 2:
            if isinstance(args[0], (str, text_type)):
                self.content_type = args[0].strip()
            if isinstance(args[1], dict):
                kwargs.update(args[1])

        if len(args) == 1:
            if isinstance(args[0], (str, text_type)):
                self.content_type = args[0].strip()
            if isinstance(args[0], dict):
                kwargs.update(args[0])

        self.content_type = kwargs.pop("Content_Type", None) or self.content_type

        self.fvars = dict(self.fvars, **kwargs)

        from .. import http
        if 'headers' in http.request and self.content_type:
            http.header("Content-type", self.content_type, unique=True)

        env = self.make_env(out, *args, **self.fvars)
        if isinstance(self.source_code, (str, text_type)):
            code = compile(self.source_code, self.filename, 'exec')
        exec(code, env)
        return out.getvalue()
