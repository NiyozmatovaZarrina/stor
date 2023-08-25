from django.urls import path, include
from rest_framework import routers
from .views import PrihoddetailViewSet

router = routers.DefaultRouter()
router.register(r'Prihoddetail', PrihoddetailViewSet)

urlpatterns = [
    path("", include(router.urls)),    
]
