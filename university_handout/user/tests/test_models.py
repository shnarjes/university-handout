from django.test import TestCase

from user.models.user import User
from user.models.otp import OTP
from user.utils.utils import create_end_time, end_time


class UserTest(TestCase):

    def setUp(self):
        return User.objects.create(
            first_name='narjes',
            last_name='sh',
            phone='09023916857',
            email='narjes1379sh@gmail.com'
        )

    def test_user_creation(self):
        user = User.objects.get(phone='09023916857')
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.__str__(), user.phone)


class OTPTest(TestCase):

    def setUp(self):
        user = User.objects.create(
            first_name='narjes',
            last_name='sh',
            phone='09023916857',
            email='narjes1379sh@gmail.com'
        )
        return OTP.objects.create(
            code='123456',
            exp_time=create_end_time(),
            exp_time_error_send=end_time(),
            exp_time_error_verified=end_time(),
            user=user,
            type=1,
            number_error_3time=0,
            number_error_5time=0
        )

    def test_OTP_creation(self):
        otp = OTP.objects.get(code='123456')
        self.assertTrue(isinstance(otp, OTP))
        self.assertEqual(otp.__str__(), otp.code)
