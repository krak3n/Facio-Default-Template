#!/usr/bin/env python
# encoding: utf-8
"""
common.py

Common {{PROJECT_NAME}} settings that apply to all environments.
"""

from os.path import abspath, join, dirname

""" Paths """
# Root of the site (not project)
SITE_ROOT = abspath(join(dirname(__file__), '..', '..'))
# Root of the project
PROJECT_ROOT = abspath(join(dirname(__file__), '..'))
# Variable Media (Uploaded content via the cms etc)
MEDIA_ROOT = join(SITE_ROOT, 'media')
# Static Dirs - as of django 1.3
STATICFILES_DIRS = [
    join(PROJECT_ROOT, 'public'),]
# Log files
LOG_ROOT = join(SITE_ROOT, 'logs')

""" Urls """
# Static Media URL
STATIC_URL = '/s/'
# Variable Media URL
MEDIA_URL = '/m/'
# Admin static media URL
ADMIN_MEDIA_PREFIX = '/s/admin/'
# Root URL config
ROOT_URLCONF = '{{PROJECT_NAME}}.urls'

""" Secret Key & Site ID """
SITE_ID = 1
SECRET_KEY = '{{DJANGO_SECRET_KEY}}'

""" Location """
TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en-gb'
USE_I18N = True
USE_L10N = True

""" Templates """
TEMPLATE_DIRS = [join(PROJECT_ROOT, 'templates')]
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    # Custom Request Contexts, add your own as required
    '{{PROJECT_NAME}}.context_processors.domain',
)

""" Middleware """
MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

""" Installed Applications """
INSTALLED_APPS = (
    # Django Apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    # Third Party Apps here
    # Project Apps here
)
