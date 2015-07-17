# coding=utf-8
"""Docstring for this file."""
__author__ = 'Christian Christelis <christian@kartoza.com>'
__project_name = 'data_captor'
__filename = 'urls'
__doc__ = ''

"""URI Routing configuration for this apps."""
from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(
        r'^(?P<imei>[\d]+)$',
        'data_captor.views.add_reading'
    ),
)
