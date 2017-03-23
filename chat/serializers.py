# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import serializers

from chat.models import Message
from accounts.serializers import UserSerializer


class MessageSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    text = serializers.CharField()

    class Meta:
        model = Message
        fields = ('user', 'text', 'time',)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
