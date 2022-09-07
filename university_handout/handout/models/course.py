from django.db import models
from django.utils.translation import gettext_lazy as _

from handout.models.major_minor import Minor


class Course(models.Model):
    minor = models.ForeignKey(
        Minor,
        verbose_name=_('Minor'),
        on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=255)
    logo = models.ImageField(
        _('Logo'), upload_to='storage/logo', null=True, blank=True)

    class Meta:
        verbose_name = _('course')
        verbose_name_plural = _('courses')
        unique_together = (
            'minor',
            'title'
        )
        ordering = ('title',)

    def __str__(self):
        return self.title
