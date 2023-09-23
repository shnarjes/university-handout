
import random
from datetime import timedelta
from kavenegar import *
from celery import shared_task

from django.utils import timezone


STATUS_CHOICES = {
    'register': 'Your verification code for register: ',
    'login': 'Your verification code for login: ',
}


@shared_task
def send_sms_otp(mobile, token):
    try:
        api = KavenegarAPI()#Id be posted
        params = {
            'receptor': mobile,
            'template': 'verify',
            'token': token,
            'type': 'sms',  # sms vs call
        }
        api.verify_lookup(params)

    except APIException as e:
        print(e.args[0].decode("utf-8"))

    except HTTPException as e:
        print(e)


def randN(N):
    min = pow(10, N-1)
    max = pow(10, N) - 1
    return random.randint(min, max)


def create_end_time():
    return timezone.now() + timedelta(minutes=3)


def end_time():
    return timezone.now() + timedelta(minutes=60)
