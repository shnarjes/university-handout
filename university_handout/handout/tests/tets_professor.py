from time import time
from functools import wraps
from rest_framework.test import APIClient

from django.urls import reverse
from django.test import TestCase

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


class ProfessorTest(TestCase):

    def setUp(self):
        Professor.objects.create(name='narjes')
        Professor.objects.create(name='mahsa')

    @not_more_than(0.09)
    def test_list(self):
        response = self.client.get(reverse('handout:professor-list'))
        professor = Professor.objects.all().count()
        self.assertEqual(response.data['count'], professor)

    @not_more_than(0.09)
    def test_retrieve(self):
        professor = Professor.objects.get(name='narjes')
        response = APIClient().get(reverse('handout:professor-detail', args=(professor.id,)))
        self.assertEqual(response.data['name'], professor.name)

    @not_more_than(0.09)
    def test_search(self):
        url = '{url}?{filter}={value}'.format(
            url=reverse('handout:professor-list'),
            filter='search', value='narjes')
        response = self.client.get(url)
        professor = Professor.objects.filter(
            name__icontains='narjes',
            title__icontains='narjes',
        ).count()
        self.assertEqual(response.data['count'], professor)
