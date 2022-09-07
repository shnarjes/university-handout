
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from handout.serializers import HandoutSerializer
from handout.models.handout import Handout


# class CustomFilter(django_filters.FilterSet):
#     category = django_filters.ModelChoiceFilter(field_name="category__title",)
#     year = django_filters.DateFilter(field_name='year')
#     course = django_filters.CharFilter(field_name='course__title', )
#     professor = django_filters.CharFilter(field_name='professor__name', )
#     university = django_filters.CharFilter(field_name='university__name', )


#     class Meta:
#         model = Handout
#         fields = ['year', 'category__title', 'course', 'professor', 'university']


class HandoutAPIViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Handout.objects.handouts_select_related()
    serializer_class = HandoutSerializer
    permission_classes = (AllowAny, )
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filter_class = CustomFilter
    search_fields = (
        'title',
        'category__title',
        'course__title',
        'course__minor__title',
        'course__minor__major__title',
        'professor__name',
        'university__name',
        'university__type__title',
        'author',
        'description',
    )
    filterset_fields = (
        'year',
        'category__title',
        'course__title',
        'professor__name',
        'university__name',
    )
    ordering_fields = (
        'category',
        'course',
        'professor',
        'university',
        'year',

    )
    ordering = ('upload_datetime', )
