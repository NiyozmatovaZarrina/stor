from django.urls import path, include
from rest_framework import routers

from .views import PrihoddetailViewSet

router = routers.DefaultRouter()
router.register("prihoddetail", PrihoddetailViewSet, "prihoddetail")

urlpatterns = [
    path('', include(router.urls))
]
