#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

# Temporary setting while playing with config:
LOAD_CONTENT_CACHE = False

AUTHOR = u'Thomas Barclay'
SITENAME = u'Kepler &amp; K2'
BANNER_SUBTITLE = u"Science Center Website"
SITEURL = ''
SITELOGO = 'images/NASA_logo_vector_lg.png'
SITELOGO_SIZE = 32
FAVICON = 'image/Kepler_K2_logos_transp.png'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

THEME = "themes/pelican-bootstrap3-kepler"
BOOTSTRAP_THEME = 'flatly'
BOOTSTRAP_FLUID = False

BANNER = "/images/K2-sc-galacticcoords.png"
HIDE_SITENAME = False

DISPLAY_TAGS_ON_SIDEBAR = False

IGNORE_FILES = [
    "README.md",
]


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_BREADCRUMBS = True
HIDE_SIDEBAR = True
MD_EXTENSIONS = (['toc'])

PLUGIN_PATHS = [os.path.join(os.path.dirname(os.path.realpath(__file__)), "plugins")]
PLUGINS = ['extract_toc']

MENUITEMS = (
        ('News', '/'),
        ('Mission', (
            ('Science', 'BROKEN'),
            ('Submenu 2', 'BROKEN'),
            ('Submenu 3', 'BROKEN'),
            )
        ),
        ('K2 Observing', 'pages/k2-observing.html'),
        ('Data analysis', 'BROKEN'),
        ('Helpdesk', 'BROKEN'),
        )

RELATEDSITES = (
            ('Kepler Website @ NASA', 'http://www.nasa.gov/mission_pages/kepler/main/index.html'),
            ('Education &amp; Outreach @ NASA', 'http://kepler.arc.nasa.gov'),
            ('Mission Manager Updates @ NASA', 'http://www.nasa.gov/mission_pages/kepler/news/mmu.html'),
            ('K2 Data Archive @ MAST', 'http://archive.stsci.edu/k2'),
            ('Kepler Data Archive @ MAST', 'http://archive.stsci.edu/kepler'),
            ('NASA Exoplanet Archive @ IPAC', 'http://exoplanetarchive.ipac.caltech.edu'),
            )

SHOW_ARTICLE_AUTHOR = True

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
