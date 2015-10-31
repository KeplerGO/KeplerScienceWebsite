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
#SITENAME = u'Kepler &amp; K2'
#BANNER_SUBTITLE = u"Science Center Website"
SITENAME = "Kepler &amp; K2"
BANNER_SUBTITLE = "Science Center"
SITEURL = ''
SITELOGO = 'images/NASA_logo_vector_lg.png'
SITELOGO_SIZE = 32
#FAVICON = 'images/Kepler_K2_logos_transp.png'
FAVICON = 'images/favicon.png'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'

PATH = 'content'
THEME = "themes/pelican-bootstrap3-kepler"
BOOTSTRAP_THEME = 'flatly'
BOOTSTRAP_FLUID = False

BANNER = "images/Fergal-galacticcoords-27May-redo30Oct-sc-tb.png"
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
            ('Targets & programs', 'k2-approved-programs.html'),
            ('Microlensing experiment', 'k2-c9.html'),
            ('Proposal preparation', 'k2-proposing-targets.html'),
            ('Discretionary time','k2-ddt.html'),
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

KEY_INFORMATION = (
            ('K2: Fields', 'k2-fields.html'),
            ('K2: Proposing targets', 'k2-proposing-targets.html'),
            ('K2: Discretionary time', 'k2-ddt.html'),
            ('Kepler/K2: Data products', 'data-products.html'),
            ('Kepler/K2: Publications', 'publications.html'),
            )

IMPORTANT_DATES = (
            ('<b>29 Oct 2015</b>',
             'K2 Campaign 5 data release (expected)',
             'data-products.html#k2-product-overview'),
            ('<b>10 Dec 2015</b>',
             'K2 DDT proposals due for Campaign 9',
             'k2-ddt.html'),
            ('<b>01 Jan 2016</b>',
             'K2 Campaign 6 data release (expected)',
             'data-products.html#k2-product-overview'),
            ('<b>Feb 2016</b>',
             'K2 Campaigns 11-13 proposal deadline',
             'k2-proposing-targets.html#campaigns-11-12-13'),
            ('<b>10 Mar 2016</b>',
             'K2 DDT proposals due for Campaign 10',
             'k2-ddt.html'),
            ('<b>28 Mar 2016</b>',
             'K2 Campaign 7 data release (expected)',
             'data-products.html#k2-product-overview'),
         )

MEETINGS = (
            ('<b>2-5 Nov 2015</b><br>'
             'K2 Science Conference',
             'http://lcogt.net/k2scicon/'),
            ('<b>10 Nov 2015</b><br>'
             'K2 Workshop at the DPS',
             'special-k2-workshop-at-the-dps-on-10-november-2015.html'),
             ('<b>16-18 Nov 2015</b><br>'
             'Enabling Transiting Exoplanet Science with JWST',
             'http://www.cvent.com/events/enabling-transiting-exoplanet-science-with-jwst/event-summary-122488a7d40e4953adc6dda02f02a643.aspx'),
            ('<b>29 Nov - 4 Dec 2015</b><br>'
             'Extreme Solar Systems III',
             'http://ciera.northwestern.edu/Hawaii2015.php'),
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
DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

DATE_MODIFIED = datetime.datetime.now().strftime('%Y-%m-%d')
