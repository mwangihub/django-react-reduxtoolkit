from django.urls import path
from . import auth_views as auth

urlpatterns = [
    path("v1/check-auth/", auth.CheckAuthentication.as_view(), name="check_auth"),
    path("v1/login/", auth.LoginView.as_view(), name="login"),
    path("v1/logout/", auth.LogOutView.as_view(), name="logout"),
]
