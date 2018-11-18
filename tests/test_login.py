from django.test import TestCase
from django.test import Client
from . make_user import make_user


class TestLoginUser(TestCase):

    def setUp(self):
        self.client = Client()

    def test_user_can_login(self):
        user = make_user(email='testuser@email.com', username='honey', password='default')
        response = self.client.post('/api/login', {
            'email': 'testuser@email.com',
            'username': 'honey',
            'password': 'default'
        })
        parsed_response = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual('testuser@email.com', parsed_response.get('email'))
        self.assertEqual('default', parsed_response.get('password'))
        self.assertTrue('token' in parsed_response)
        self.assertTrue('token')

    def test_invalid_response_on_invalid_data(self):
        user = make_user(username='honey', password='default')
        response = self.client.post('/api/login', {'username': 'honey', 'password': 'badpass'})
        parsed_response = response.json()
        self.assertEqual(response.status_code, 401)
        self.assertTrue('errors' in parsed_response)
