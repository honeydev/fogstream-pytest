from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User


class TestRegisterUser(TestCase):

    def setUp(self):
        self.client = Client()


    def test_register_valid_user(self):
        response = self.client.post('/api/register', {
            'email': 'testuser@email.com',
            'username': 'testuser@email.com',
            'password': 'default',
            'password_repeat': 'default'
        })

        parsed_response = response.json()
        self.assertTrue(User.objects.filter(email='testuser@email.com').count())
        self.assertEqual('testuser@email.com', parsed_response['email'])
        print(parsed_response)

    def test_password_not_equal_error(self):

        response = self.client.post('/api/register', {
            'email': 'testuser@email.com',
            'username': 'testuser@email.com',
            'password': 'default',
            'password_repeat': 'not_default'
        })

        parsed_response = response.json()
        print(parsed_response)
        self.assertEqual(response.status_code, 401)
        self.assertTrue(
            "Entered passwords is not euqal default not_default" in parsed_response['errors']['non_field_errors']
        )