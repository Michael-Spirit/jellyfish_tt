# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import serializers

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'is_superuser', 'first_name', 'last_name', 'email',
                  'username', 'is_active',)
