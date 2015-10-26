#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import datetime

DEVMODE = True  # Shows a red warning message at the top

if DEVMODE:
    ANALYTICS = ()
else:
    ANALYTICS = ("""<script language="javascript" id="_fed_an_ua_tag" src="//dap.digitalgov.gov/Universal-Federated-Analytics-Min.js?agency=NASA"></script>""",
                 """<script language="javascript" id="_fed_an_ua_tag" src="//dap.digitalgov.gov/Universal-Federated-Analytics-Min.js?agency=NASA&subagency=ARC&dclink=true"></script>""")

# Temporary setting while playing with config:
LOAD_CONTENT_CACHE = False

AUTHOR = u'Thomas Barclay'
SITENAME = u'Kepler &amp; K2'
BANNER_SUBTITLE = u"Science Center Website"
SITEURL = ''
SITELOGO = 'images/NASA_logo_vector_lg.png'
SITELOGO_SIZE = 32
FAVICON = 'images/Kepler_K2_logos_transp.png'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'

PATH = 'content'
THEME = "themes/pelican-bootstrap3-kepler"
BOOTSTRAP_THEME = 'flatly'
BOOTSTRAP_FLUID = False

BANNER = "images/K2-sc-galacticcoords.png"
HIDE_SITENAME = False

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

# Which static data dirs should be uploaded as part of the website?
STATIC_PATHS = ['images', 'data']

# Directories that contain html files we want to exclude
# (because they are sub-pages included through rst includes)
PAGE_EXCLUDES = ['pages/k2-observing/approved-programs']

PLUGIN_PATHS = [os.path.join(os.path.dirname(os.path.realpath(__file__)), "plugins")]
PLUGINS = ['extract_toc']

STATIC_PATHS = (['images', 'data'])

MENUITEMS = (
        ('News', 'archives.html'),
        ('The missions', (
            ('Overview', 'the-missions.html'),
            ('Science', 'the-science.html'),
            ('Publications', 'publications.html'),
            ('Conferences', 'conferences.html'),
            )
        ),
        ('K2 observing', (
            ('Overview', 'k2-observing.html'),
            ('Campaign fields', 'k2-fields.html'),
            ('Technical information', 'k2-photometric-performance.html'),
            ('Targets & programs', 'k2-approved-programs.html'),
            ('Microlensing experiment', 'k2-c9.html'),
            ('Proposal preparation', 'k2-proposing-targets.html'),
            ('DDT program','k2-ddt.html'),
            )
        ),
        ('Data analysis', (
            ('Data releases', 'data-releases.html'),
            ('Data access', 'data-access.html'),
            ('Pipeline', 'pipeline.html'),
            ('Software', 'software.html'),
            )
        ),
        )

KEY_INFORMATION = (
            ('K2 Campaign fields', 'k2-fields.html'),
            ('K2 approved programs', 'k2-approved-programs.html'),
            ('K2 proposal preparation', 'k2-proposing-targets.html'),
            ('K2 DDT program','k2-ddt.html'),
            ('Data access', 'data-access.html'),
            ('Recent publications', 'publications.html'),
            )

IMPORTANT_DATES = (
            ('<b>29 Oct 2015</b><br>'
             'K2 Campaign 5 data release (expected)',
             'data-releases.html#k2-product-overview'),
            ('<b>10 Dec 2015</b><br>'
             'K2 DDT proposals due for Campaign 9',
             'k2-ddt.html'),
            ('<b>01 Jan 2016</b><br>'
             'K2 Campaign 6 data release (expected)',
             'data-releases.html#k2-product-overview'),
            ('<b>Feb 2016</b><br>'
             'K2 Campaigns 11-13 proposal deadline',
             'k2-proposing-targets.html#campaigns-11-12-13'),
            ('<b>10 Mar 2016</b><br>'
             'K2 DDT proposals due for Campaign 10',
             'k2-ddt.html'),
            ('<b>28 Mar 2016</b><br>'
             'K2 Campaign 7 data release (expected)',
             'data-releases.html#k2-product-overview'),
         )

MEETINGS = (
            ('<b>2-5 Nov 2015</b><br>'
             'K2 Science Conference',
             'http://lcogt.net/k2scicon/'),
            ('<b>8-13 Nov 2015</b><br>'
             '47th DPS Meeting',
             'http://aas.org/meetings/dps47'),
            ('<b>9-10 Dec 2015</b><br>'
             '5th Australian Exoplanet Workshop',
             'http://astronomy.swin.edu.au/planets/FifthWorkshop2015/'),
            ('<b>4-8 Jan 2015</b><br>'
             '227th AAS meeting',
             'http://aas.org/meetings/aas227'),
            ('<b>11-15 Jul 2016</b><br>'
             'KASC Asteroseismology Workshop',
             'http://www.cadc-ccda.hia-iha.nrc-cnrc.gc.ca/en/meetings/getMeetings.html?number=4796'),
        )

RELATEDSITES = (
            ('Kepler Website @ NASA',
             'http://www.nasa.gov/mission_pages/kepler/main/index.html'),
            ('Kepler Education &amp; Outreach @ NASA',
             'http://kepler.arc.nasa.gov'),
            ('Mission Manager Updates @ NASA',
             'http://www.nasa.gov/mission_pages/kepler/news/mmu.html'),
            ('Kepler/K2 Website @ Ball Aerospace',
             'http://www.ballaerospace.com/page.jsp?page=72'),
            ('Kepler Data Archive @ MAST',
             'http://archive.stsci.edu/kepler'),
            ('K2 Data Archive @ MAST',
             'http://archive.stsci.edu/k2'),
            ('NASA Exoplanet Archive @ IPAC',
             'http://exoplanetarchive.ipac.caltech.edu'),
            )

SHOW_ARTICLE_AUTHOR = True
DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

DATE_MODIFIED = datetime.datetime.now().strftime('%Y-%m-%d')
