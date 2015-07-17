__author__ = 'Christian Christelis <christian@kartoza.com>'
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from django.core import serializers

from data_captor.models import Captor
from data_captor.models import Reading


@api_view(['POST'])
def add_reading(request, imei):
    captor = get_object_or_404(Captor, imei=imei)
    data = request.POST
    reading = Reading(captor=captor)
    reading.mode = data.get('mode')
    reading.location = 'POINT(%s %s)' % (data['latitude'], data['longitude'])
    reading.altitude = data['altitude']
    reading.time = data['time']
    reading.save()

    serialized_obj = serializers.serialize('json', [reading, ])

    return HttpResponse(serialized_obj, content_type='application/json')



