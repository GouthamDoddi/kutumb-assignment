from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


# PROFILE_URL=reverse('')

# class TestingTheUserModel(TestCase):
#     """Here we will create various methods that can perform tests"""
#     def setUp(self):
#         """Here we will set up the user and login him"""
#         user = get_user_model().objects.create_user('testman', 'testpass123')
#         self.client = Client()
#         self.client.force_authenticate(user)
#         self.client.save()
