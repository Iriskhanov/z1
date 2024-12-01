from django.urls import path, include
from rest_framework.routers import DefaultRouter
from property.api.views import PropertyViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet, basename='property')

urlpatterns = [
    path('', include(router.urls)),
]
