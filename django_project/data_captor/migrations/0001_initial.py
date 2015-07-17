# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Captor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imei', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mode', models.CharField(max_length=1)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('altitude', models.FloatField(null=True, blank=True)),
                ('time', models.DateTimeField()),
                ('num_of_satellites', models.IntegerField(null=True, blank=True)),
                ('speed', models.FloatField(null=True, blank=True)),
                ('course', models.FloatField(null=True, blank=True)),
                ('gsm_location', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
                ('gsm_time', models.DateTimeField(null=True, blank=True)),
                ('captor', models.ForeignKey(to='data_captor.Captor')),
            ],
        ),
    ]
