from time import time
from functools import wraps
from rest_framework.test import APIClient

from django.urls import reverse
from django.test import TestCase

from handout.models.university import University, UniversityType


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


class UniTest(TestCase):

    def setUp(self):
        type1 = UniversityType.objects.create(title='title1')
        type2 = UniversityType.objects.create(title='title2')
        University.objects.create(name='sku', type=type2)
        University.objects.create(name='stu', type=type1)

    @not_more_than(0.09)
    def test_list(self):
        response = self.client.get(reverse('handout:uni-list'))
        uni = University.objects.all().count()
        self.assertEqual(response.data['count'], uni)

    @not_more_than(0.09)
    def test_retrieve(self):
        uni = University.objects.get(name='sku')
        response = APIClient().get(reverse('handout:uni-detail', args=(uni.id,)))
        self.assertEqual(response.data['name'], uni.name)

    @not_more_than(0.09)
    def test_filter(self):
        url = '{url}?{filter}={value}'.format(
            url=reverse('handout:uni-list'),
            filter='type__title', value='title1')
        response = self.client.get(url)
        uni = University.objects.filter(type__title='title1').count()
        self.assertEqual(response.data['count'], uni)

    @not_more_than(0.09)
    def test_search(self):
        url = '{url}?{filter}={value}'.format(
            url=reverse('handout:uni-list'),
            filter='search', value='sku')
        response = self.client.get(url)
        uni = University.objects.filter(
            name__contains='sku',
            # type__title__contains='sku',
        ).count()
        self.assertEqual(response.data['count'], uni)

    @not_more_than(0.09)
    def test_order(self):
        url = '{url}?{filter}={value}'.format(
            url=reverse('handout:uni-list'),
            filter='ordering', value='type')
        response = self.client.get(url)
        response_results = response.json().get('results')
        uni = University.objects.get(type__title='title1')
        self.assertEqual(response_results[0]['name'], uni.name)
