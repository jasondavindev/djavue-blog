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
        # r1 = client.post('/api/signup', { 'username': 'test', 'password': 'test', 'email': 'test@mail.com', 'firstname': 'test', 'lastname': 'bot' })
        r2 = client.post('/api/login', { 'username': 'test', 'password': 'test' })
        r3 = client.post('/api/logout')
        
        # self.assertEqual(200, r1.status_code)
        # self.assertEqual(True, r1.json()['created'])
        self.assertNotEqual(None, r2.content)
        self.assertNotEqual(None, r3.content)
