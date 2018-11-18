from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth.models import User
from . serializers import CreateContactMessageSerializer
from . mailer import AdminContactMessageMailer


class CreateContactMessage(APIView):

    auth = JSONWebTokenAuthentication()
    mailer = AdminContactMessageMailer()

    def post(self, request):
        '''
        :param request:
        :raise MailException
        :return: Request
        '''
        request_data = request.data
        data = self.auth.authenticate(request)

        if not data:
            return Response({'errors': "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)

        username = data[0]
        user = User.objects.get(username=username)
        serializer_context = {'author': user}

        serializer = CreateContactMessageSerializer(data=request_data, context=serializer_context)
        serializer.is_valid()

        if (serializer.errors):
            return Response({"errors": serializer.errors}, status.HTTP_400_BAD_REQUEST)
        contact_message = serializer.save()
        self.mailer.send(contact_message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
