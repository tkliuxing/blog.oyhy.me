#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = "themes/pelican-clean-blog"
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = False

AUTHOR = 'Ronald White'
SITENAME = 'OYHY.ME'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('看小说么？', 'http://www.kanxiaoshuo.me/'),
         )

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 7

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }

GITHUB_URL = 'http://github.com/tkliuxing'
WEIBO_URL = 'http://weibo.com/oyhy'
FACEBOOK_URL = 'http://facebook.com/oyhyo'

COLOR_SCHEME_CSS = 'monokai.css'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
