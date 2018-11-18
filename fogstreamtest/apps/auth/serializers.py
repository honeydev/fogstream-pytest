from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from fogstreamtest.apps.auth.jwt import JWT


class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField(max_length=255, required=False)
    username = serializers.CharField(max_length=128, required=True)
    password = serializers.CharField(max_length=128, required=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        '''
        :param object data:
        :return: dictionary
        '''
        email = data.get('email')
        password = data.get('password')
        username = data.get('username')
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError('A user with this username and password was not found.')
        jwt = JWT(user)
        return {
            'email': email,
            'password': password,
            'username': username,
            'token': jwt.generate()
        }


class RegisterSerializer(serializers.Serializer):

    email = serializers.EmailField(max_length=255, required=True)
    username = serializers.CharField(max_length=128, required=True)
    password = serializers.CharField(max_length=128, required=True)
    password_repeat = serializers.CharField(max_length=128, required=False)

    def validate(self, data):
        '''
        :param object data:
        :return: dictionary
        '''
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')
        password_repeat = data.pop('password_repeat', None)
        if password != password_repeat:
            raise serializers.ValidationError('Entered passwords is not euqal {} {}'.format(password, password_repeat))

        if User.objects.filter(username=username).count():
            raise serializers.ValidationError('User with username {} already exists'.format(username))

        return data

    def create(self, validated_data):
        '''
        :param dictionary validated_data:
        :return: User
        '''
        return User.objects.create_user(**validated_data)
