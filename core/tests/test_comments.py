from core.models import User
from django.test.client import Client
from django.test.testcases import TestCase
from core.tests import fixtures
from core.models import Post
import json


class TestAuthApi(TestCase):
    @classmethod
    def setUpTestData(cls):
        fixtures.create_user()

    def test_auth_api(self):
        client = Client()
        client.force_login(User.objects.get(username='test'))

        client.post('/api/posts', fixtures.get_post())
        r2 = client.post('/api/comments', fixtures.get_comment())

        self.assertEqual(1, r2.json()['id'])