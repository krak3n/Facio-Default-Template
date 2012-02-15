#!/usr/bin/env python
# encoding: utf-8
"""
settings.py

Settings for stage environment for {{PROJECT_NAME}}.
"""


from {{PROJECT_NAME}}.config.common import *


""" STATIC_ROOT as of django 1.3 """
STATIC_ROOT = join(PROJECT_ROOT, 'static')


""" Debugging (default True for stage environment) """
DEBUG = True
TEMPLATE_DEBUG = DEBUG


""" Databases (default is mysql) """
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_pass',
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