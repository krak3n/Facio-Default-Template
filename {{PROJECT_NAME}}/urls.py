#!/usr/bin/env python
# encoding: utf-8
"""
urls.py

Root URL config for {{PROJECT_NAME}}.
"""


from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin


""" django admin is installed by default """
admin.autodiscover()


""" Root URL patterns """
urlpatterns = patterns('',
    # Example:
    # (r'^app_name/', include('{{PROJECT_NAME}}.app_name.urls')),
    # django admin
    (r'^admin/', include(admin.site.urls)),
)


""" Media Serving - Debug Mode """
if settings.DEBUG:
    
    # Serving static and variable media e.g /s/images/some_image.jpg
    urlpatterns += patterns('django.views.static',
        url(r'^%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'), 'serve', {'document_root': settings.STATIC_ROOT}),
        url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'), 'serve', {'document_root': settings.MEDIA_ROOT}),
    )
    
    # Preview for 404 and 500 pages
    urlpatterns += patterns('',
        url(r'^404/$', direct_to_template, {'template': '404.html'}, name='404'),
        url(r'^500/$', direct_to_template, {'template': '500.html'}, name='500'),
    )