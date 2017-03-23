# -*- coding: utf-8 -*-
import factory

from accounts.tests.factories import UserFactory
from chat.models import Message


class MessageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Message

    user = factory.SubFactory(UserFactory)
    text = factory.Faker("text")
    time = factory.Faker("time")
