from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination

from handout.serializers import ProfessorSerializer
from handout.models.professor import Professor


class ProfessorAPIViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = (AllowAny, )
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('name', 'title')
