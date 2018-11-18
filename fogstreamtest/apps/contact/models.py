from django.db import models
from django.contrib.auth.models import User


class ContactMessage(models.Model):

    title = models.CharField(db_index=True, max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    created_at = models.DateTimeField(auto_now_add=True)
    mail_send = models.BooleanField(default=False)

    @classmethod
    def create(cls, title, body):
        contact_message = cls(title=title)
        contact_message = cls(body=body)
        print('contact message', contact_message)
        return contact_message
