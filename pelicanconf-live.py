"""This config is used when you run `make html-live` or `make live`.

It inherits most of the settings from pelicanconf.py.
"""
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.
import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

CACHE_CONTENT = False

ANALYTICS = ("""<script language="javascript" id="_fed_an_ua_tag" src="//dap.digitalgov.gov/Universal-Federated-Analytics-Min.js?agency=NASA"></script>""",
             """<script language="javascript" id="_fed_an_ua_tag" src="//dap.digitalgov.gov/Universal-Federated-Analytics-Min.js?agency=NASA&subagency=ARC&dclink=true"></script>""")
