from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CVViewSet

router = DefaultRouter()
router.register("cv", CVViewSet, basename="cv")

urlpatterns = [
    path("", include(router.urls)),
]
