#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import datetime

# Temporary setting while playing with config:
LOAD_CONTENT_CACHE = False

AUTHOR = u'Thomas Barclay'
SITENAME = u'Kepler &amp; K2'
BANNER_SUBTITLE = u"Science Center Website"
SITEURL = ''
SITELOGO = 'images/NASA_logo_vector_lg.png'
SITELOGO_SIZE = 32
FAVICON = 'images/Kepler_K2_logos_transp.png'

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

DISPLAY_BREADCRUMBS = False

HIDE_SIDEBAR = True
MD_EXTENSIONS = (['toc'])

STATIC_PATHS = ['images', 'data']

# Directories that contain html files we want to exclude (because they are included indirectly)
PAGE_EXCLUDES = ['pages/k2-observing/approved-programs']

PLUGIN_PATHS = [os.path.join(os.path.dirname(os.path.realpath(__file__)), "plugins")]
PLUGINS = ['extract_toc']

STATIC_PATHS = (['images', 'data'])

MENUITEMS = (
        ('News', 'archives.html'),
        ('The missions', (
            ('Submenu 1', 'pages/k2-observing.html'),
            ('Submenu 2', 'pages/k2-observing.html'),
            ('Submenu 3', 'pages/k2-observing.html'),
            )
        ),
        ('K2 observing', (
            ('Overview', 'k2-observing.html'),
            ('Photometric performance', 'k2-photometric-performance.html'),
            ('Campaign fields', 'k2-fields.html'),
            ('How to propose targets?', 'k2-proposing-targets.html'),
            ('Approved programs', 'k2-approved-programs.html'),
            )
        ),
        ('Data analysis', (
            ('Submenu 1', 'pages/k2-observing.html'),
            ('Submenu 2', 'pages/k2-observing.html'),
            ('Submenu 3', 'pages/k2-observing.html'),
            )
        ),
        )
#  ('Helpdesk', 'BROKEN'),

KEY_INFORMATION = (
            ('K2 Campaign fields', 'pages/k2-campaign-fields.html'),
            ('Data access', 'http://TBD'),
            ('Recent publications', 'http://TBD'),
            )

IMPORTANT_DATES = (
            ('<b>18 Sep 2015</b><br>K2 Science Conference abstract and hotel reservation deadline ', 'http://lcogt.net/k2scicon/'),
            ('<b>28 Sep 2015</b><br>K2 Campaign 4 data release (expected)', ''),
            ('<b>25 Dec 2015</b><br>K2 Campaign 5 data release (expected)', ''),
            
         )

MEETINGS = (('<b>13-15 Oct 2015</b><br>Kepler Exoplanet Populations Hack Week', 'http://keplerscience.arc.nasa.gov/KeplerHackWeek/'),
            ('<b>18-22 Oct 2015</b><br>RR Lyrae 2015 Conference', 'http://rrl2015.hu/'),
            ('<b>2-5 Nov 2015</b><br>K2 Science Conference', 'http://lcogt.net/k2scicon/'),
            ('<b>8-13 Nov 2015</b><br>K2 workshop at the annual DPS meeting', 'http://aas.org/meetings/dps47'),
         )

RELATEDSITES = (
            ('Kepler Website @ NASA', 'http://www.nasa.gov/mission_pages/kepler/main/index.html'),
            ('Kepler Education &amp; Outreach @ NASA', 'http://kepler.arc.nasa.gov'),
            ('Mission Manager Updates @ NASA', 'http://www.nasa.gov/mission_pages/kepler/news/mmu.html'),
            ('Kepler Data Archive @ MAST', 'http://archive.stsci.edu/kepler'),
            ('K2 Data Archive @ MAST', 'http://archive.stsci.edu/k2'),
            ('NASA Exoplanet Archive @ IPAC', 'http://exoplanetarchive.ipac.caltech.edu'),
            )

TWITTER_USERNAME = "KeplerGO"
TWITTER_WIDGET_ID = "631217672827437056"

DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
GITHUB_USER = False

SHOW_ARTICLE_AUTHOR = True

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

DATE_MODIFIED = datetime.datetime.now().strftime('%Y-%m-%d')
