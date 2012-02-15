#!/usr/bin/env python
# encoding: utf-8
"""
context_processors.py

Custom context processors. Add your own as required.
"""


from django.conf import settings
from django.contrib.sites.models import Site


def domain(request):
    """ Add DOMAIN to context """
    
    current_site = Site.objects.get_current()
    domain = getattr(settings, 'DOMAIN', 'http://%s' % current_site.domain)
    return {
        'DOMAIN': domain,
        'site': current_site,
    }