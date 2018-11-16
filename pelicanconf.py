#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import datetime
import pelican

# If `DEVMODE = True`, show a red warning banner at the top
DEVMODE = False   # pelicanconf-dev.py will override this

# By default, use agressive caching.
# The Makefile ensures we use `--ignore-cache` for production builds.
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True
CHECK_MODIFIED_METHOD = 'mtime'
CONTENT_CACHING_LAYER = 'generator'  # This causes an empty news page
WITH_FUTURE_DATES = False

ANALYTICS = ()   # pelicanconf-live.py will override this

AUTHOR = u'Geert Barentsen'
SITENAME = "Kepler &amp; K2"
BANNER_SUBTITLE = "Science Center"
SITEURL = "https://keplerscience.arc.nasa.gov"
SITELOGO = 'images/NASA_logo_vector_lg.png'
SITELOGO_SIZE = 32
FAVICON = 'images/favicon.png'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'

PATH = 'content'
THEME = "themes/pelican-bootstrap3-kepler"
BOOTSTRAP_THEME = 'flatly'
BOOTSTRAP_FLUID = False

BANNER = "images/kepler-k2-banner.jpg"
HIDE_SITENAME = False

IGNORE_FILES = [
    "README.md",
]

# Enable RSS feeds
FEED_DOMAIN = "https://keplerscience.arc.nasa.gov"
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS = "feeds/all.rss.xml"
# We don't need per-author or per-category or per-translation feeds
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_BREADCRUMBS = False

HIDE_SIDEBAR = True

if pelican.__version__ >= '3.7.0':
    MARKDOWN = {
        'extension_configs': {
            'markdown.extensions.toc': {},
            'markdown.extensions.codehilite': {'css_class': 'highlight'},
            'markdown.extensions.extra': {},
            'markdown.extensions.meta': {},
        },
    }
else:
    MD_EXTENSIONS = (['toc'])


# Which static data dirs should be uploaded as part of the website?
STATIC_PATHS = (['images', 'data'])

# Directories that contain html files we want to exclude
# because they are sub-pages included through rst includes
PAGE_EXCLUDES = ['pages/k2-observing/approved-programs']

# The fancy table of contents sidebar requires a plugin
PLUGIN_PATHS = [os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             "plugins")]
PLUGINS = ['extract_toc']

# Defines the menu items in the top bar
MENUITEMS = (
        ('News', 'archives.html'),
        ('The missions', (
            ('Objectives', 'objectives.html'),
            ('Telescope', 'the-kepler-space-telescope.html'),
            ('Science', 'science.html'),
            ('Publications', 'publications.html'),
            ('Conferences', 'conferences.html'),
            ('Users Panel', 'users-panel.html'),
            )
         ),
        ('K2 observing', (
            ('Overview', 'k2-observing.html'),
            ('Campaign fields', 'k2-fields.html'),
            ('Targets &amp; programs', 'k2-approved-programs.html'),
            ('Data release notes', 'k2-data-release-notes.html'),
            ('Proposal preparation', 'k2-proposing-targets.html'),
            ('C9 Microlensing experiment', 'k2-c9.html'),
            ('C16 Supernova experiment', 'supernova-experiment'),
            )
         ),
        ('Data analysis', (
            ('Data products', 'data-products.html'),
            ('Pipeline', 'pipeline.html'),
            ('Software', 'software.html'),
            ('Community products', 'community-products.html'),
            )
         ),
        )

# Defines the "key information" box on the front page
KEY_INFORMATION = (
            ('K2: Campaign fields', 'k2-fields.html'),
            ('K2: Observed programs', 'k2-approved-programs.html'),
            ('Kepler/K2: Data products', 'data-products.html'),
            )

# Defines the "important dates" box on the front page
IMPORTANT_DATES = (
            ('<b>15 Jan 2019</b>',
             'Poster deadline for Kepler & K2 SciCon V',
             'scicon-2019/index.html'),
         )

# Defines the "meetings" box on the front page
MEETINGS = (
            ('<b>6–10 Jan 2019</b><br>'
             'Kepler/K2 Booth at #AAS233',
             'https://aas.org/meetings/aas233'),
            ('<b>10 Jan 2019</b><br>'
             'Kepler/K2 Special Session at #AAS233',
             'two-kepler-special-sessions-at-the-winter-aas.html'),
            ('<b>4-8 Mar 2019</b><br>'
             'Kepler & K2 Sci Con V (Glendale)',
             'scicon-2019/index.html')
            )

# Defines the "related websites" listing in the footer of all pages
RELATEDSITES = (
            ("Kepler/K2 News and Media Resources",
             'http://www.nasa.gov/kepler'),
            ('Kepler/K2 @ Ball Aerospace',
             'http://www.ballaerospace.com/page.jsp?page=72'),
            ('Kepler Data Archive @ MAST',
             'http://archive.stsci.edu/kepler'),
            ('K2 Data Archive @ MAST',
             'http://archive.stsci.edu/k2'),
            ('NASA Exoplanet Archive @ IPAC',
             'http://exoplanetarchive.ipac.caltech.edu'),
            )

SHOW_ARTICLE_AUTHOR = True
DEFAULT_PAGINATION = 10

RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

DATE_MODIFIED = datetime.datetime.now().strftime('%Y-%m-%d')
