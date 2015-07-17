# coding=utf-8
__author__ = 'Christian Christelis <christian@kartoza.com>'

from django.contrib.gis.db import models


class Captor(models.Model):
    """Uniquely identify a data captor.
    """
    imei = models.CharField(max_length=15)

    class Meta:
        app_label = 'data_captor'


class Reading(models.Model):
    """A new reading.
    """
    captor = models.ForeignKey(Captor)
    mode = models.CharField(max_length=1)
    location = models.PointField()
    altitude = models.FloatField(null=True, blank=True)
    time = models.DateTimeField()
    num_of_satellites = models.IntegerField(null=True, blank=True)
    speed = models.FloatField(null=True, blank=True)
    course = models.FloatField(null=True, blank=True)
    gsm_location = models.PointField(null=True, blank=True)
    gsm_time = models.DateTimeField(null=True, blank=True)

    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'data_captor'

