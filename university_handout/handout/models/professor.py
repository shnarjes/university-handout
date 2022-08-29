from django.db import models
from django.utils.translation import gettext_lazy as _


class Professor(models.Model):
    name = models.CharField(_('Name'), max_length=255, unique=True)
    picture = models.ImageField(
        _('Picture'), upload_to='storage/picture', null=True, blank=True)

    TITLE_CHOICES = (
        ('دکتر', 'دکتر'),
        ('مهندس', 'مهندس'),
        ('آقای', 'آقای'),
        ('خانم', 'خانم')
    )

    title = models.CharField(_('Title'), max_length=20,
                             choices=TITLE_CHOICES, default='دکتر')

    class Meta:
        verbose_name = _('Professor')
        verbose_name_plural = _('Professors')
        ordering = ('name',)

    def __str__(self):
        return self.name
