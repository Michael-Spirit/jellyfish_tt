# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url

urlpatterns = [
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),
]
