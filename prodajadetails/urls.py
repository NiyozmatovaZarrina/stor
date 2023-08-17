from django.urls import path, include
from rest_framework import routers

from .views import ProdajadetailViewSet

router = routers.DefaultRouter()
router.register("prodajadetail", ProdajadetailViewSet, "prodajadetail")

urlpatterns = [
    path('', include(router.urls))
]
