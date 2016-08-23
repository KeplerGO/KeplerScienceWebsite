"""This config is used when you run `make github`.

It inherits most of the settings from pelicanconf.py.
"""
from __future__ import unicode_literals

# First load all the defaults from pelicanconf.py
import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

CACHE_CONTENT = False

# Then override anything we want to override below:
DEVMODE = True  # This will add the big red warning banner at the top
