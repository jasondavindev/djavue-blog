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
        r2 = client.get('/api/posts')
        posts = r2.json()['posts']
        r3 = client.get('/api/posts/%d' % posts[0]['id'])
        r4 = client.get('/api/posts/%d/like' % posts[0]['id'])
        r5 = client.delete('/api/posts/%d' % posts[0]['id'])
        
        self.assertEqual(True, 'created' in r1.json().keys())
        self.assertEqual(1, len(posts))
        self.assertEqual(True, 'post' in r3.json())
        self.assertEqual(True, r4.json()['liked'])
        self.assertEquals(True, r5.json()['deleted'])
