from django.urls import path, include
from rest_framework import routers

from .views import ProduktViewSet

router = routers.DefaultRouter()
router.register("produkt", ProduktViewSet, "produkt")

urlpatterns = [
    path('', include(router.urls))
]
