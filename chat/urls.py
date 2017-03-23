# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url

from rest_framework import routers

from chat.views import MessageAPI

router = routers.DefaultRouter()
router.register(r'messages', MessageAPI, 'message')

urlpatterns = router.urls
