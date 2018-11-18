from django.contrib.auth.models import User, Group
from rest_framework import serializers
from fogstreamtest.apps.auth.jwt import JWT
from . models import ContactMessage

class CreateContactMessageSerializer(serializers.Serializer):

    title = serializers.CharField(max_length=50, required=True)
    body = serializers.CharField(max_length=500)

    def validate(self, data):
        '''
        :param data:
        :return: dictionary
        '''
        title = data.get('title')
        body = data.get('body')

        return data

    def create(self, validated_data):
        '''
        :param dictionary validated_data:
        :return: ContactMessage
        '''
        author = self.context.get('author', None)
        return ContactMessage.objects.create(author_id=author.id, **validated_data)
