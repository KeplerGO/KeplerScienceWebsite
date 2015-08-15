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
        ('K2 observing', 'pages/k2-observing.html'),
        ('Data analysis', 'BROKEN'),
        )
#  ('Helpdesk', 'BROKEN'),

QUICK_LINKS = (
            ('K2 Campaigns list', 'http://TBD'),
            ('Publication database', 'http://TBD'),
            )

IMPORTANT_DATES = (
            ('<b>9 Sep 2015</b><br>K2 Sci Con registration deadline', 'http://TBD'),
            ('<b>10 Feb 2016</b><br>Campaigns 10-12 proposal deadline', 'http://TBD'),
            ('<b>3 Mar 2016</b><br>Campaign 12 data release', 'http://TBD'),
         )

MEETINGS = (
            ('<b>2-6 Nov 2015</b><br>K2 Science Conference', 'http://TBD'),
            ('<b>12 Dec 2015</b><br>K2 session at the DPS meeting', 'http://TBD'),
            ('<b>14 Dec 2015</b><br>RR Lyrae stars conference', 'http://TBD'),
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

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
