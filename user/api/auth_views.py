from django.conf import settings
from django.contrib import auth
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from importlib import import_module


def response_object(
    req, ok_msg: str = "", err_msg: str = "", status=status.HTTP_200_OK
):
    if req.user.is_authenticated:
        return Response(
            {
                "isAuthenticated": True,
                "details": {
                    "user": req.user.email,
                    "message": ok_msg,
                },
            },
            status,
        )
    return Response(
        {
            "isAuthenticated": False,
            "details": {
                "user": None,
                "message": err_msg,
            },
        },
        status,
    )


def import_callable(path_or_callable):
    if hasattr(path_or_callable, "__call__"):
        return path_or_callable
    else:
        assert isinstance(path_or_callable, str)
        package, attribute = path_or_callable.rsplit(".", 1)
        return getattr(import_module(package), attribute)


settings_serializers = getattr(settings, "REST_AUTH_SERIALIZERS", {})
# LoginSerializer = import_callable(
#     settings_serializers.get("LOGIN_SERIALIZER", DefaultLoginSerializer)
# )


@method_decorator(csrf_exempt, name="dispatch")
class CheckAuthentication(APIView):
    permission_classes = [
        permissions.AllowAny,
    ]

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return response_object(request, ok_msg="Already authenticated")
        return response_object(
            request, err_msg="Not authenticated", status=status.HTTP_404_NOT_FOUND
        )


@method_decorator(csrf_protect, name="dispatch")
class LoginView(APIView):

    permission_classes = [
        permissions.AllowAny,
    ]
    # serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data["email"]
        password = request.data["password"]
        user = auth.authenticate(email=email, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return response_object(request, ok_msg="Authentication successful")
        return response_object(
            request,
            err_msg="Authentication failed, check your credentials",
            status=status.HTTP_401_UNAUTHORIZED,
        )


@method_decorator(csrf_exempt, name="dispatch")
class LogOutView(APIView):
    permission_classes = [
        permissions.AllowAny,
    ]

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            auth.logout(request)
        return response_object(
            request, ok_msg="Logout successful", status=status.HTTP_200_OK
        )
