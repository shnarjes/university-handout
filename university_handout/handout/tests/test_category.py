from time import time
from functools import wraps
from rest_framework.test import APIClient

from django.urls import reverse
from django.test import TestCase

from handout.models.category import Category


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


class CategoryTest(TestCase):

    def setUp(self):
        Category.objects.create(title='title1')
        Category.objects.create(title='titleman')

    @not_more_than(0.09)
    def test_list(self):
        response = self.client.get(reverse('handout:category-list'))
        category = Category.objects.all().count()
        self.assertEqual(response.data['count'], category)

    @not_more_than(0.09)
    def test_retrieve(self):
        category = Category.objects.get(title='title1')
        response = APIClient().get(reverse('handout:category-detail', args=(category.id,)))
        self.assertEqual(response.data['title'], category.title)

    @not_more_than(0.09)
    def test_search(self):
        url = '{url}?{filter}={value}'.format(
            url=reverse('handout:category-list'),
            filter='search', value='man')
        response = self.client.get(url)
        category = Category.objects.filter(
            title__icontains='man',
        ).count()
        self.assertEqual(response.data['count'], category)
