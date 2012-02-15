#!/usr/bin/env python
# encoding: utf-8
"""
settings.py

Local settings for {{PROJECT_NAME}}.
"""


from {{PROJECT_NAME}}.config.common import *


""" Debugging (default True for local environment) """
DEBUG = True
TEMPLATE_DEBUG = DEBUG


""" Databases (default is mysql) """
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{{DB_NAME}}',
        'USER': '{{DB_USER}}',
        'PASSWORD': '{{DB_PASS}}',
    }
}


""" Admins """
ADMINS = (('Name', 'email@email.com'),)
MANAGERS = ADMINS


""" Cacheing (default is dummy, see django docs) """
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
