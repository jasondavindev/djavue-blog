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

        r1 = client.post('/api/posts', fixtures.get_post())
        # r1 = client.post('/api/add_todo', {'new_task': 'walk the dog'})
        # r2 = client.post('/api/add_todo', {'new_task': 'do the laundry'})
        # r3 = client.get('/api/list_todos')
        # self.assertEqual({200}, {r.status_code for r in [r1, r2, r3]})
        # todos = json.loads(r3.content.decode('utf-8'))
        # self.assertEqual(2, len(todos['todos']))
        # self.assertEqual(True, r1.json().has_key('posts'))

