from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from user.manager import UserManager


class User(AbstractUser):
    phone = models.CharField(
        _('Phone'),
        max_length=11,
        unique=True,
    )
    email = models.EmailField(_('email address'))

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    objects = UserManager()
    username = None

    class Meta:
        app_label = 'user'
        verbose_name = "user"
        verbose_name_plural = " users"

    def __str__(self) -> str:
        return str(self.phone)
