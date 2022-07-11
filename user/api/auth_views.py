from django.conf import settings
from django.contrib import auth
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt, get_token
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import auth_serializers as serializers

from api_auth.serializers import LoginSerializer as DefaultLoginSerializer
from importlib import import_module


def import_callable(path_or_callable):
    if hasattr(path_or_callable, '__call__'):
        return path_or_callable
    else:
        assert isinstance(path_or_callable, str)
        package, attribute = path_or_callable.rsplit('.', 1)
        return getattr(import_module(package), attribute)


settings_serializers = getattr(settings, 'REST_AUTH_SERIALIZERS', {})
LoginSerializer = import_callable(settings_serializers.get('LOGIN_SERIALIZER', DefaultLoginSerializer))


@method_decorator(ensure_csrf_cookie, name="dispatch")
class GetCSRFTOKENView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, *args, **kwargs):
        token = get_token(request)
        return Response({'token': "Cookie set"}, status=status.HTTP_200_OK)


@method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    """
        The post function is used to log in a user. It takes the username and password as input from the user and authenticates it using django's built-in authentication function. If the authentication is successful, then it returns a response with status code 200 OK else it returns an error message.
        :param self: Refer to the class instance itself, and is used to access variables that belongs to the class
        :param request: Get the data that is sent to the server by the client
        :param *args: Send a non-keyworded variable length argument list to the function
        :param **kwargs: Pass a keyworded, variable-length argument list
        :return: A response object
        :doc-author: Trelent
        """
    permission_classes = [permissions.AllowAny, ]
    serializer_class = LoginSerializer


    def post(self, request, *args, **kwargs):
        print(request.data)
        email = request.data['email']
        password = request.data['password']
        user = auth.authenticate(email=email, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return Response({"details": "authentication successful"}, status=status.HTTP_200_OK)
        return Response({"details": "wrong credentials"}, status=status.HTTP_401_UNAUTHORIZED)
