# coding=utf-8
__author__ = 'Christian Christelis <christian@kartoza.com>'

from django.contrib.gis import admin
from data_captor.models import Captor, Reading


admin.site.register(Captor)
admin.site.register(Reading)
