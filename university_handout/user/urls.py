from django.urls import path
from user.views.register import RegisterAPIView
from user.views.login import LoginAPIView
from user.views.verified_code import VerifiedAPI

app_name = "user"

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('verified', VerifiedAPI.as_view(), name='verified'),
]
