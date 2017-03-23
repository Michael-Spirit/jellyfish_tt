# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status

from accounts.tests.factories import UserFactory, User

TEST_EMAIL = 'test@example.com'
TEST_USERNAME = 'username'
TEST_PASSWORD = 'TestPassword1'


class TestAccountAPI(APITestCase):

    def test_api_login(self):
        """
        Test API user login successful
        """
        user = UserFactory(
            email=TEST_EMAIL,
            username=TEST_USERNAME,
            password=TEST_PASSWORD
        )

        data = {
            'email': TEST_EMAIL,
            'username': TEST_USERNAME,
            'password': TEST_PASSWORD,
        }

        url = reverse('rest_login')
        response = self.client.post(url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['key'], user.auth_token.key)

    def test_sign_up(self):
        """
        Test API user register successful
        """
        self.assertEqual(User.objects.count(), 0)

        data = {
            'email': TEST_EMAIL,
            'username': TEST_USERNAME,
            'password1': TEST_PASSWORD,
            'password2': TEST_PASSWORD
        }

        url = reverse('rest_register')
        response = self.client.post(url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

    def test_logout(self):
        """
        TEST API user logout successful
        """
        user = UserFactory()
        self.client.force_authenticate(user=user)

        response = self.client.post(reverse('rest_logout'), format='json')
        self.assertEqual(response.data['detail'], 'Successfully logged out.')
