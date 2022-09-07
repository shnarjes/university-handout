from rest_framework import routers
from django.urls import path, include

from handout.views.handout_views import HandoutAPIViewSet
from handout.views.category_views import CategoryAPIViewSet
from handout.views.university_view import UniversityAPIViewSet
from handout.views.professor_views import ProfessorAPIViewSet

app_name = "handout"

router = routers.SimpleRouter()
router.register('handout', HandoutAPIViewSet, basename='handout')
router.register('category', CategoryAPIViewSet, basename='category')
router.register('university', UniversityAPIViewSet, basename='uni')
router.register('professor', ProfessorAPIViewSet, basename='professor')

urlpatterns = [
    path('', include(router.urls)),
    # path('^handout/by/(?P<category>\w+)/$', HandoutAPIViewSet, name='handout')
    # path('category', CategoryAPIViewSet,name='category')
]
