from django.db import models
from django.utils.translation import gettext_lazy as _


class Major(models.Model):
    title = models.CharField(_('Title'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('Major')
        verbose_name_plural = _('Majors')
        ordering = ('title',)

    def __str__(self):
        return self.title


class Minor(models.Model):
    major = models.ForeignKey(
        Major,
        verbose_name=_('Major'),
        on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('Minor')
        verbose_name_plural = _('Minors')
        ordering = ('title',)

    def __str__(self):
        return self.title
