#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import datetime

# If `DEVMODE = True`, show a red warning banner at the top
DEVMODE = False   # pelicanconf-dev.py will override this

CACHE_CONTENT = True

ANALYTICS = ()   # pelicanconf-live.py will override this

AUTHOR = u'Thomas Barclay'
SITENAME = "Kepler &amp; K2"
BANNER_SUBTITLE = "Science Center"
SITEURL = "http://keplerscience.arc.nasa.gov"
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
FEED_DOMAIN = "http://keplerscience.arc.nasa.gov"
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS = "feeds/all.rss.xml"
# We don't need per-author or per-category or per-translation feeds
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_BREADCRUMBS = False

HIDE_SIDEBAR = True
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
            )
         ),
        ('K2 observing', (
            ('Overview', 'k2-observing.html'),
            ('Campaign fields', 'k2-fields.html'),
            ('Targets &amp; programs', 'k2-approved-programs.html'),
            ('Microlensing experiment', 'k2-c9.html'),
            ('Proposal preparation', 'k2-proposing-targets.html'),
            ('Discretionary time', 'k2-ddt.html'),
            )
         ),
        ('Data analysis', (
            ('Data products', 'data-products.html'),
            ('Pipeline', 'pipeline.html'),
            ('Software', 'software.html'),
            ('Related surveys', 'related-surveys.html'),
            )
         ),
        )

# Defines the "key information" box on the front page
KEY_INFORMATION = (
            ('K2: Campaign fields', 'k2-fields.html'),
            ('K2: Observed programs', 'k2-approved-programs.html'),
            ('K2: Proposing targets', 'k2-proposing-targets.html'),
            ('K2: Discretionary time', 'k2-ddt.html'),
            ('Kepler/K2: Data products', 'data-products.html'),
            ('Kepler/K2: Publications', 'publications.html'),
            )

# Defines the "important dates" box on the front page
IMPORTANT_DATES = (
            ('<b>25 Jan 2016</b>',
             'K2 Campaign 6 data release (expected)',
             'data-products.html#k2-product-overview'),
            ('<b>5 Feb 2016</b>',
             'K2 Campaigns 11-13 proposals due (step 1)',
             'k2-proposing-targets.html#campaigns-11-12-13'),
            ('<b>10 Mar 2016</b>',
             'K2 Campaign 10 DDT proposals due',
             'k2-ddt.html'),
            ('<b>28 Mar 2016</b>',
             'K2 Campaign 7 data release (expected)',
             'data-products.html#k2-product-overview'),
            ('<b>19 Jun 2016</b>',
             'K2 Campaign 8 data release (expected)',
             'data-products.html#k2-product-overview'),
         )

# Defines the "meetings" box on the front page
MEETINGS = (
            ('<b>9-10 Dec 2015</b><br>'
             '5th Australian Exoplanet Workshop',
             'http://astronomy.swin.edu.au/planets/FifthWorkshop2015/'),
            ('<b>5 Jan 2015</b><br>'
             'K2 Special Session @ #AAS227',
             'http://keplerscience.arc.nasa.gov/k2-special-session-at-aas227-on-5-jan-2016.html'),
            ('<b>13-15 Jan 2016</b><br>'
             'K2 Session @ 20th Microlensing Workshop',
             'http://www.iap.fr/microlensing2016/'),
            ('<b>11-15 Jul 2016</b><br>'
             'TASC2-KASC9 Asteroseismology Workshop',
             'http://www.iastro.pt/research/conferences/spacetk16/')
            )

# Defines the "related websites" listing in the footer of all pages
RELATEDSITES = (
            ("Kepler/K2 News and Media Resources",
             'http://www.nasa.gov/mission_pages/kepler/main/index.html'),
            ('Kepler/K2 Education Resources',
             'http://kepler.arc.nasa.gov'),
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
