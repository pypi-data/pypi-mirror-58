#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Utilities for make the code run both on Python2 and Python3.
"""
import sys

PY2 = sys.version_info[0] == 2

# urljoin
if PY2:
    from urlparse import urljoin
else:
    from urllib.parse import urljoin

# urlencode
if PY2:
    from urllib import urlencode
else:
    from urllib.parse import urlencode

# Dictionary iteration
if PY2:
    iterkeys = lambda d: d.iterkeys()
    itervalues = lambda d: d.itervalues()
    iteritems = lambda d: d.iteritems()
else:
    iterkeys = lambda d: iter(d.keys())
    itervalues = lambda d: iter(d.values())
    iteritems = lambda d: iter(d.items())

# string and text types
try:
    text_type = unicode
    string_types = (str, unicode)
    numeric_types = (int, long)
except NameError:
    text_type = str
    string_types = (str,)
    numeric_types = (int,)

if PY2:
    is_iter = lambda x: x and hasattr(x, "next")
else:
    is_iter = lambda x: x and hasattr(x, "__next__")

# imap
if PY2:
    from itertools import imap
else:
    imap = map

# quote & unquote
if PY2:
    import urlparse
    from urllib import quote, unquote
else:
    from urllib.parse import quote, unquote
    from urllib import parse as urlparse

# StringIO
if PY2:
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO
else:
    from io import StringIO

# BytesIO
if PY2:
    try:
        from cStringIO import StringIO as BytesIO
    except ImportError:
        from StringIO import StringIO as BytesIO
else:
    from io import BytesIO
