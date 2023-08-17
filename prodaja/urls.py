from django.urls import path, include
from rest_framework import routers

from .views import ProdajaViewSet

router = routers.DefaultRouter()
router.register("prodaja", ProdajaViewSet, "prodaja")

urlpatterns = [
    path('', include(router.urls))
]
