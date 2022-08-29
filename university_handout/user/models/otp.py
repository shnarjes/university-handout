from django.db import models
from django.utils.translation import gettext_lazy as _
from user.models.user import User


class OTPType(models.IntegerChoices):
    REGISTER = (1, _("REGISTER"))
    LOGIN = (2, _("LOGIN"))


class OTP(models.Model):
    code = models.CharField(
        max_length=11,
        verbose_name=_("code"),
        help_text=_("code"),
        unique=True
        )
    exp_time = models.DateTimeField(
        verbose_name=_("exp_time"),
        help_text=_("Time out")
        )
    exp_time_error_send = models.DateTimeField(
        verbose_name=_("exp_time_error_send"),
        help_text=_("Time to resend the code"),
        null=True,
        blank=True
        )
    exp_time_error_verified = models.DateTimeField(
        verbose_name=_("exp_time_error_verified"),
        help_text=_("Time to code confirmation"),
        null=True,
        blank=True
        )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="otp_user",
        verbose_name=_("user"),
        help_text=_("user")
        )
    number_error_3time = models.PositiveIntegerField(
        verbose_name=_("number_error_3time"),
        help_text=_("number of time enter the code"),
        null=True,
        blank=True
    )
    number_error_5time = models.PositiveIntegerField(
        verbose_name=_("number_error_5time"),
        help_text=_("number of time send the code"),
        null=True,
        blank=True
    )
    type = type = models.IntegerField(
        choices=OTPType.choices,
        verbose_name=_("type"),
        help_text=_("type")
    )

    def __str__(self):
        return self.code
