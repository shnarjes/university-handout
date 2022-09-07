from django.db import models
from django.utils.translation import gettext_lazy as _

from handout.manager import CustomManager


class UniversityType(models.Model):
    title = models.CharField(_('Title'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('University Type')
        verbose_name_plural = _('Universitie Types')
        ordering = ('title',)

    def __str__(self):
        return self.title


class University(models.Model):
    name = models.CharField(_('Name'), max_length=255, unique=True)
    logo = models.ImageField(
        _('Logo'), upload_to='storage/logo', null=True, blank=True)
    type = models.ForeignKey(UniversityType, verbose_name=_(
        'Type'), on_delete=models.CASCADE)

    objects = CustomManager()

    class Meta:
        verbose_name = _('University')
        verbose_name_plural = _('Universities')
        ordering = ('name',)

    def __str__(self):
        return self.name
