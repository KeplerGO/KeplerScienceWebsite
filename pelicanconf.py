#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Thomas Barclay'
SITENAME = u'Kepler and K2'
BANNER_SUBTITLE = u"Guest Observer Office Blog"
SITEURL = ''
SITELOGO = 'images/NASA_logo_vector_lg.png'
SITELOGO_SIZE = 32
FAVICON = 'image/Kepler_K2_logos_transp.png'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

#THEME = "/Users/tom/websites/K2MicrolensingWorkshop/tom-themes/gum"
THEME = "/Users/tom/gitcode/pelican-bootstrap3"
BOOTSTRAP_THEME = 'flatly'
BOOTSTRAP_FLUID = False

BANNER = "/images/K2-sc-galacticcoords.png"
HIDE_SITENAME = False

DISPLAY_TAGS_ON_SIDEBAR = False


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Subscribe', 'http://keplerscience.arc.nasa.gov/NewsExploder.shtml'),
		('Kepler Science Center', 'http://keplerscience.arc.nasa.gov/'),
         ('K2 Science Center', 'http://keplerscience.arc.nasa.gov/K2'),
         ('Mission Manager Updates', 'http://www.nasa.gov/mission_pages/kepler/news/mmu.html'))

SHOW_ARTICLE_AUTHOR = True

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
