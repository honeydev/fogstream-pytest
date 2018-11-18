from fogstreamtest.apps.auth.jwt import JWT
from django.contrib.auth.models import User
from django.test import TestCase
from . make_user import make_user
from django.test import Client
from rest_framework_jwt.serializers import (
    JSONWebTokenSerializer, RefreshJSONWebTokenSerializer,
    VerifyJSONWebTokenSerializer
)


class TestJwt(TestCase):

    def test_jwt_generate(self):
        user = make_user(username='testuser@email.com', password='default')
        jwt = JWT(user)

        token = jwt.generate()
        self.assertTrue(isinstance(token, str))
        #assert token is not empty string
        self.assertTrue(token)


    def test_jwt_decode(self):
        user = make_user(username='testuser@email.com', password='default')
        jwt = JWT(user)
        token = jwt.generate()
        c = Client()
        response = c.post('/api/post/create', {'data': 'data'}, HTTP_AUTHORIZATION='JWT ' + token)
