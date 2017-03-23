# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status

from accounts.tests.factories import UserFactory, User
from chat.tests.factories import MessageFactory, Message


class TestMessageAPI(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)

    def test_add_message(self):
        """
        TEST API add message
        """
        url = reverse("chat:message-list")
        data = {
            "text": "hello world"
        }

        response = self.client.post(url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.first().text, data['text'])

    def test_add_message_for_unauth_user(self):
        """
        Test fail add message if user not logged in
        """
        pass

    def test_update_message(self):
        """
        Test PATCH user message
        """
        pass

    def test_fail_update_other_user_message(self):
        """
        Test fail to PATCH another user message
        """
        pass

    def test_delete_message(self):
        """
        Test DELETE user message
        """
        pass

    def test_fail_delete_other_user_message(self):
        """
        Test fail to DELETE another user message
        """
        pass
