from django.contrib import admin

from user.models.user import User
from user.models.otp import OTP


admin.site.register(User)
admin.site.register(OTP)
