
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
        api = KavenegarAPI('5356454B5438394A397A396C6C5564504966785464413374456C7359723531354F344547627954597036553D')
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
