# -*- coding: utf-8 -*-

import sys

PY_3 = sys.version_info.major == 3

if PY_3:
    utf8 = lambda s: s
else:
    utf8 = lambda s: s.decode('utf-8')
