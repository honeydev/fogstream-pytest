from django.conf import settings
from django.core.mail import EmailMessage
from .exceptions import MailException


class AdminContactMessageMailer:

    def send(self, contact_message):
        '''
        :param ContactMessage contact_message:
        :raise MailException
        :return: None
        '''
        subject = contact_message.title
        body = contact_message.body
        mail_status = EmailMessage(subject=subject, body=body, to=[x[1] for x in settings.ADMINS]).send()
        if mail_status:
            contact_message.mail_send = True
            contact_message.save()
        else:
            raise MailException("Failed send message for admins")
