from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (
    LoginSerializer, RegisterSerializer
)


class LoginView(APIView):

    def post(self, request):
        '''
        :param request:
        :return: Response
        '''
        request_data = request.data
        serializer = LoginSerializer(data=request_data)
        serializer.is_valid()
        if serializer.errors:
            print(serializer.errors)
            return Response({"errors": serializer.errors}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.data, status=status.HTTP_200_OK)


class RegisterView(APIView):

    def post(self, request):
        '''
        :param request:
        :return: Response
        '''
        request_data = request.data
        serializer = RegisterSerializer(data=request_data)
        serializer.is_valid()

        if serializer.errors:
            return Response({"errors": serializer.errors}, status=status.HTTP_401_UNAUTHORIZED)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

