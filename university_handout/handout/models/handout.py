import uuid
import os
from django.db import models
from django.utils.translation import gettext_lazy as _

from handout.models.category import Category
from handout.models.course import Course
from handout.models.professor import Professor
from handout.models .university import University
from handout.manager import CustomManager


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(uuid.uuid4())[:8], ext)
    return os.path.join('storage/handout', filename)


class Handout(models.Model):
    category = models.ForeignKey(
        Category,
        related_name=('category'),
        verbose_name=_('Category'),
        on_delete=models.CASCADE
        )
    course = models.ForeignKey(
        Course,
        verbose_name=_('Course'),
        on_delete=models.CASCADE
        )
    file = models.FileField(
        _('File'),
        upload_to=get_file_path)
    year = models.IntegerField(_('Year'), null=True, blank=True)
    professor = models.ForeignKey(
        Professor,
        verbose_name=_('Professor'),
        on_delete=models.SET_NULL,
        null=True,
        blank=True)
    university = models.ForeignKey(
        University,
        verbose_name=_('University'),
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    author = models.CharField(
        _('Author'),
        max_length=255,
        null=True,
        blank=True)

    description = models.TextField(
        _('Description'),
        null=True,
        blank=True)
    upload_datetime = models.DateTimeField(
        _('Upload Datetime'),
        auto_now_add=True)
    title = models.CharField(_('Title'), max_length=255, null=True, blank=True)

    add_datetime = models.DateTimeField(_('Add Datetime'), auto_now_add=True)
    modify_datetime = models.DateTimeField(_('Modify Datetime'), auto_now=True)

    logo = models.ImageField(
        _('Logo'), upload_to='storage/logo', null=True, blank=True)

    is_processed = models.BooleanField(_('Is Processed'), default=False)

    objects = CustomManager()

    class Meta:
        verbose_name = _('handout')
        verbose_name_plural = _('handouts')
        ordering = ('-upload_datetime',)

    def __str__(self):
        return self.file.name

    def save(self, *args, **kwargs):
        if not self.id:
            description = ''

            self.title = '{} {}'.format(self.category.title, self.course.title)

            if self.professor:
                self.title += '  {} {}'.format(
                    self.professor.title,
                    self.professor.name
                )
                description += '{} {}'.format(
                    self.professor.title, self.professor.name)

            description += '\n{}، {}'.format(
                self.course.minor.major.title, self.course.minor.title)

            if self.university:
                description += '\n' + self.university.name

            if self.author:
                description += '\n' + self.author

            if self.description:
                self.description = description + '\n' + self.description
            else:
                self.description = description
        return super(Handout, self).save(*args, **kwargs)
