# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin


urlpatterns = patterns(
    '',
    # Enable the admin:
    url(r'^data-captor-admin/', include(admin.site.urls)),
    url(r'^', include('data_captor.urls', namespace='data-captor')),
)

# expose static files and uploaded media if DEBUG is active
if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {
                'document_root': settings.MEDIA_ROOT,
                'show_indexes': True
            }),
        url(r'', include('django.contrib.staticfiles.urls'))
    )
