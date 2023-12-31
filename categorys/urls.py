from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet

router = routers.DefaultRouter()
router.register(r'Category', CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),    
]
