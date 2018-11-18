from fogstreamtest.apps.auth.jwt import JWT
from django.contrib.auth.models import User
from django.test import TestCase


def make_user(**args):
    return User.objects.create_user(**args)