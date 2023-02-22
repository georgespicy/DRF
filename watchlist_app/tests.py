from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from watchlist_app.api import serializers
from watchlist_app import models

class StreamPlatformTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testcase', password='testcase')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token' + self.token.key)

    def test_streamplatform_create(self):
        data = {
            "name" : "netflix",
            "about": "#1 Stream Platform",
            "website" : "http://netflix.com"
        }

        response = self.client.post(reverse('streamlist-list'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_streamplatform_list(self):
        response = self.client.get(reverse('streamlist-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    