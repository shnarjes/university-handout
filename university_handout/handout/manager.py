from django.db import models


class CustomManager(models.Manager):

    def handouts_select_related(self):
        return self.get_queryset().select_related(
            'category',
            'course',
            'professor',
            'university'
        ).all()

    def university_select_related(self):
        return self.get_queryset().select_related('type',).all()
