from django.urls import path, include
from rest_framework import routers 
from .views import AgentViewSet


router = routers.DefaultRouter()
router.register(r'agents', AgentViewSet)

urlpatterns = [
    path("", include(router.urls)),    
]