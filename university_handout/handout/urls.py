from rest_framework import routers

from django.urls import path

from handout.views.category_view import CategoryAPIViewSet


app_name = "handout"

router = routers.SimpleRouter()
router.register('category', CategoryAPIViewSet, basename='category')
urlpatterns = router.urls
