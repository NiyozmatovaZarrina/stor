from django.urls import path, include
from rest_framework import routers
from .views import PrihodViewSet

router = routers.DefaultRouter()
router.register(r'Prihod', PrihodViewSet)

urlpatterns = [
   path("", include(router.urls)),   
]
