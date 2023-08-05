#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import simplejson as json
except ImportError:
    import json

import functools

from datetime import (
    datetime,
    date
)


class JsonExtendEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(o, date):
            return o.strftime("%Y-%m-%d")
        elif hasattr(o, 'isoformat'):
            return o.isoformat()
        return json.JSONEncoder.default(o)


def jsonresult(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        return ('text/json; charset=utf-8', json.dumps(r, cls=JsonExtendEncoder))

    return _wrapper


def textresult(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        return ('text/plain', str(r))

    return _wrapper


if __name__ == "__main__":
    pass
