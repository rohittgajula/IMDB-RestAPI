from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authtoken.models import Token

from .serializers import RegestrationSerializer
from user_app import models


@api_view(['POST', ])
def logout_view(request):

    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['POST', ])
def registration_view(request):

    if request.method == 'POST':
        data = request.data
        serializer = RegestrationSerializer(data=data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()       # over-riding save method to add extra field "PASSWORD2"            
    
            # we need to over-ride save method, all the current functionality will be there and we can add some more according to out requirement.

            data['response'] = "Registration Sucessfull."
            data['username'] = account.username
            data['email'] = account.email               # store all this data into data{}

            token = Token.objects.get(user=account).key     # getting token.
            data['token'] = token

        else:
            data = serializer.errors

        return Response(data)
        