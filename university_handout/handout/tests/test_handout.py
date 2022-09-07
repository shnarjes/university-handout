from time import time
from functools import wraps
from rest_framework.test import APIClient

from django.urls import reverse
from django.test import TestCase

from handout.models.handout import Handout, get_file_path
from handout.models.category import Category
from handout.models.course import Course
from handout.models.major_minor import Minor, Major
from handout.models.professor import Professor


def not_more_than(normal_duration):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time()
            result = func(*args, **kwargs)
            duration = time() - start_time
            assert duration <= normal_duration, f"<{func._name_}>'s duration is {duration} that is more than {normal_duration}"

            return result

        return wrapper

    return decorator


class HandoutTest(TestCase):

    def setUp(self):
        cat = Category.objects.create(title='title1')
        cat2 = Category.objects.create(title='titleman')
        major = Major.objects.create(title='title2')
        minor = Minor.objects.create(title='title3', major=major)
        course = Course.objects.create(title='title4', minor=minor)
        professor = Professor.objects.create(name='narjes')
        Handout.objects.create(
            title='title5',
            category=cat2,
            course=course,
            professor=professor,
            file=get_file_path(self, 'file1')
        )
        Handout.objects.create(
            title='title6',
            category=cat,
            course=course,
            professor=professor,
            file=get_file_path(self, 'file2')
        )

    @not_more_than(0.09)
    def test_list_handout(self):
        response = self.client.get(reverse('handout:handout-list'))
        handout = Handout.objects.all().count()
        self.assertEqual(response.data['count'], handout)

    @not_more_than(0.09)
    def test_retrieve_handout(self):
        handout = Handout.objects.get(id=7)
        response = APIClient().get(reverse('handout:handout-detail', args=(handout.id,)))
        self.assertEqual(response.data['title'], handout.title)

    @not_more_than(0.09)
    def test_filter(self):
        url = '{url}?{filter}={value}'.format(
            url=reverse('handout:handout-list'),
            filter='category__title', value='title1')
        response = self.client.get(url)
        handout = Handout.objects.filter(category__title='title1').count()
        self.assertEqual(response.data['count'], handout)

    @not_more_than(0.09)
    def test_search(self):
        url = '{url}?{filter}={value}'.format(
            url=reverse('handout:handout-list'),
            filter='search', value='man')
        response = self.client.get(url)
        handout = Handout.objects.filter(
            title__icontains='man',
            category__title__icontains='man',
            # course__title__icontains='man',
            # course__minor__title__icontains='man',
            # course__minor__major__title__icontains='man',
            # professor__name__search='man',
            # university__name__search='man',
            # university__type__title__search='man',
            # author__search='man',
            # description__search='man',
        ).count()
        self.assertEqual(response.data['count'], handout)

    @not_more_than(0.09)
    def test_order(self):
        url = '{url}?{filter}={value}'.format(
            url=reverse('handout:handout-list'),
            filter='ordering', value='category')
        response = self.client.get(url)
        response_results = response.json().get('results')
        handout = Handout.objects.get(category=11)
        self.assertEqual(response_results[0]['title'], handout.title)
