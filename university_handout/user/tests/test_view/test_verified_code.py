from rest_framework import status
from datetime import timedelta

from django.urls import reverse
from django.test import TestCase
from django.test.utils import override_settings

from user.models.otp import OTP
from user.models.user import User
from user.utils.utils import create_end_time, end_time, randN


class VerifiedTest(TestCase):

    @override_settings(CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
                       CELERY_ALWAYS_EAGER=True,
                       BROKER_BACKEND='memory')
    def setUp(self):
        user = User.objects.create(
            first_name='narjes',
            last_name='sh',
            phone='09903198644',
            email='narjessh@gmail.com'
        )
        OTP.objects.create(
            code=randN(6),
            exp_time=create_end_time(),
            exp_time_error_send=end_time(),
            user=user,
            type=2,
            number_error_3time=0,
            number_error_5time=0
        )

    def test_error_3time(self):
        user = User.objects.get(phone='09903198644')
        signin_dict = {
            'phone': user.phone,
            'code': '123456'
        }
        for i in range(4):
            response = self.client.post(reverse('user:verified'), signin_dict)
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)

    def test_verified_code_1hour(self):
        user = User.objects.get(phone='09903198644')
        signin_dict = {
            'phone': user.phone,
            'code': '123456'
        }
        for i in range(4):
            response = self.client.post(reverse('user:verified'), signin_dict)
        obj_otp = OTP.objects.get(user=user)
        obj_otp.exp_time_error_verified = obj_otp.exp_time_error_verified - timedelta(minutes=65)
        obj_otp.save()
        response = self.client.post(reverse('user:verified'), signin_dict)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_verified_code_accept(self):
        user = User.objects.get(phone='09903198644')
        otp = OTP.objects.get(user=user)
        signin_dict = {
            'phone': user.phone,
            'code': otp.code
        }
        response = self.client.post(reverse('user:verified'), signin_dict)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_incorrect_code(self):
        user = User.objects.get(phone='09903198644')
        signin_dict = {
            'phone': user.phone,
            'code': '123456'
        }
        response = self.client.post(reverse('user:verified'), signin_dict)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_error_exp_time(self):
        user = User.objects.get(phone='09903198644')
        otp = OTP.objects.get(user=user)
        signin_dict = {
            'phone': user.phone,
            'code': otp.code
        }
        otp.exp_time = otp.exp_time - timedelta(minutes=30)
        otp.save()
        response = self.client.post(reverse('user:verified'), signin_dict)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_not_exists(self):
        signin_dict = {
            'phone': '09023916857',
            'code': '123456'
        }
        response = self.client.post(reverse('user:verified'), signin_dict)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
