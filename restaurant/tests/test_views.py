from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(name="Item 1", price=10.99, description="Main Course")
        Menu.objects.create(name="Item 2", price=5.99, description="Appetizer")

        # Create an API client for making requests
        self.client = APIClient()
