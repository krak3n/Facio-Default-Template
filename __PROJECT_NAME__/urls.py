from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin


admin.autodiscover()
urlpatterns = patterns('')

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^404/$', direct_to_template, {'template': '404.html'},
            name='404'),
        url(r'^500/$', direct_to_template, {'template': '500.html'},
            name='500'),
        (r'^m/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )

urlpatterns = patterns(
    '',
    (r'^admin/', include(admin.site.urls)),
)
