from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination

from handout.serializers import UniversitySerializer
from handout.models.university import University


class UniversityAPIViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = University.objects.select_related('type').all()
    serializer_class = UniversitySerializer
    permission_classes = (AllowAny, )
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('name', 'type__title')
    filterset_fields = ('type__title',)
    ordering = ('type')
