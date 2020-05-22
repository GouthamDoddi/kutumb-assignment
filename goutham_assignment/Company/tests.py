from django.http import request
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.http import HttpRequest

COMPANY_DETAIL_URL = reverse('company', kwargs={'pk': 9})


class CheckingViews(TestCase):

    def test_current_views(self):
        self.client = Client()
        user1 = get_user_model().objects.create(username='testman1',
                                                password='testpass')
        self.client.force_login(user1)
        # res = HttpRequest.get(COMPANY_DETAIL_URL, user1)

