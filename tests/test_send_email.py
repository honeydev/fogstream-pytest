from django.test import TestCase
from fogstreamtest.apps.contact.mailer import AdminContactMessageMailer
from . make_user import make_user
from . make_contact import make_contact
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import send_mail


class TestAdminContactMessageMailer(TestCase):

    adminContactMessageMailer = AdminContactMessageMailer()

    def test_admin_send(self):
        user = make_user(email='test@test.com', username='test', password='12345')
        contact_message = make_contact(author=user, attributes={"title": "test title", "body": "test body"})
        mailer = AdminContactMessageMailer()
        mailer.send(contact_message)
        self.assertTrue(contact_message.mail_send)