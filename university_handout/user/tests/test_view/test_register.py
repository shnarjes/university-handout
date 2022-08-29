from rest_framework import status
from datetime import timedelta

from django.urls import reverse
from django.test import TestCase
from django.test.utils import override_settings

from user.models.user import User
from user.models.otp import OTP


class RegisterTest(TestCase):

    @override_settings(CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
                       CELERY_ALWAYS_EAGER=True,
                       BROKER_BACKEND='memory')
    def setUp(self):
        User.objects.create(
            first_name='narjes',
            last_name='sh',
            phone='09903198644',
            email='narjessh@gmail.com'
        )

    def test_error_5time_user_exists(self):
        user = User.objects.get(phone='09903198644')
        user.is_active = False
        user.save()
        signin_dict = {
            'phone': user.phone
        }
        for i in range(6):
            response = self.client.post(reverse('user:register'), signin_dict)
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)

    def test_accept_5time_user_exists(self):
        user = User.objects.get(phone='09903198644')
        user.is_active = False
        user.save()
        signin_dict = {
            'phone': user.phone
        }
        for i in range(4):
            response = self.client.post(reverse('user:register'), signin_dict)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_accept_code_1hour_user_exists(self):
        user = User.objects.get(phone='09903198644')
        user.is_active = False
        user.save()
        signin_dict = {
            'phone': user.phone
        }

        for i in range(6):
            response = self.client.post(reverse('user:register'), signin_dict)
        obj_otp = OTP.objects.get(user=user)
        obj_otp.exp_time_error_send = obj_otp.exp_time_error_send - timedelta(minutes=65)
        obj_otp.save()
        response = self.client.post(reverse('user:register'), signin_dict)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_object_otp_user_exists(self):
        user = User.objects.get(phone='09903198644')
        user.is_active = False
        user.save()
        signin_dict = {
            'phone': user.phone
        }
        response = self.client.post(reverse('user:register'), signin_dict)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_is_active_user_exists(self):
        user = User.objects.get(phone='09903198644')
        signin_dict = {
            'phone': user.phone
        }
        response = self.client.post(reverse('user:register'), signin_dict)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_error_5time_new_user(self):
        signin_dict = {
            'phone': '09023916857',
            'first_name': 'narjes',
            'last_name': 'sh',
            'email': 'narjes@gmail.com'
        }
        for i in range(6):
            response = self.client.post(reverse('user:register'), signin_dict)
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)

    def test_accept_5time_new_user(self):
        signin_dict = {
            'phone': '09023916857',
            'first_name': 'narjes',
            'last_name': 'sh',
            'email': 'narjes@gmail.com'
        }
        for i in range(4):
            response = self.client.post(reverse('user:register'), signin_dict)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_accept_code_1hour_new_user(self):
        signin_dict = {
            'phone': '09023916857',
            'first_name': 'narjes',
            'last_name': 'sh',
            'email': 'narjes@gmail.com'
        }

        for i in range(6):
            response = self.client.post(reverse('user:register'), signin_dict)
        user = User.objects.get(phone='09023916857')
        obj_otp = OTP.objects.get(user=user)
        obj_otp.exp_time_error_send = obj_otp.exp_time_error_send - timedelta(minutes=65)
        obj_otp.save()
        response = self.client.post(reverse('user:register'), signin_dict)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_object_otp_new_user(self):
        signin_dict = {
            'phone': '09023916857',
            'first_name': 'narjes',
            'last_name': 'sh',
            'email': 'narjes@gmail.com'
        }
        response = self.client.post(reverse('user:register'), signin_dict)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
