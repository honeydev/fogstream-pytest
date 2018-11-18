from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from . make_user import make_user
from fogstreamtest.apps.auth.jwt import JWT

class TestContactMessage(TestCase):

    client = Client()

    def test_create_valid_contact_message(self):
        user = make_user(email='testuser@test.com', username='testuser', password='default')
        jwt = JWT(user)
        contact_message = {"title": "test title", "body": "test body"}
        response = self.client.post('/api/contact-message/create', contact_message, HTTP_AUTHORIZATION='JWT ' + jwt.generate())
        parsed_response = response.json();
        self.assertTrue(response.status_code, 201)
        self.assertEqual(parsed_response['title'], contact_message['title'])
        self.assertEqual(parsed_response['body'], contact_message['body'])


    def test_error_on_empty_token(self):
        contact_message = {"title": "test title", "body": "test body"}
        response = self.client.post('/api/contact-message/create', contact_message)
        parsed_response = response.json()
        self.assertTrue(response.status_code, 401)
        self.assertTrue('errors' in parsed_response)
        self.assertTrue('Invalid token' in parsed_response['errors'])

    def test_error_on_invalid_request_data(self):
        user = make_user(email='testuser@test.com', username='testuser', password='default')
        jwt = JWT(user)
        contact_message = {"title": "", "body": ""}
        response = self.client.post('/api/contact-message/create', contact_message, HTTP_AUTHORIZATION='JWT ' + jwt.generate())
        parsed_response = response.json();
        self.assertTrue(response.status_code, 400)
        self.assertTrue('errors' in parsed_response)