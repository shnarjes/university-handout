from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(_('Title'), max_length=100, unique=True)
    logo = models.ImageField(
        _('Logo'), upload_to='storage/logo', null=True, blank=True)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categorys')
        ordering = ('title',)

    def __str__(self):
        return self.title
