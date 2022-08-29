from university_handout.settings.base import *
from university_handout.settings.secure import *
from university_handout.settings.packages import *
from decouple import config

DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])
