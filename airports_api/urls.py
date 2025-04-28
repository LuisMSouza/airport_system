from rest_framework.routers import DefaultRouter
from .views import AirportViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r"airports", AirportViewSet, basename="airport")
urlpatterns = [
    path("", include(router.urls)),
]
