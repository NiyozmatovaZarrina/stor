from django.urls import path, include
from rest_framework import routers
from .views import ProduktViewSet

router = routers.DefaultRouter()
router.register(r'Produkt', ProduktViewSet)

urlpatterns = [
    path("", include(router.urls)),    
]
