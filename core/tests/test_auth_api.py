from core.models import User
from django.test.client import Client
from django.test.testcases import TestCase
from core.tests import fixtures
import json


class TestAuthApi(TestCase):
    @classmethod
    def setUpTestData(cls):
        fixtures.create_user()

    def test_auth_api(self):
        client = Client()
        r2 = client.post('/api/login', { 'username': 'test', 'password': 'test' })
        r3 = client.post('/api/logout')
        
        self.assertNotEqual(None, r2.content)
        self.assertNotEqual(None, r3.content)
