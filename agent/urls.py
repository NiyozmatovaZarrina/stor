"""from django.urls import path, include
from rest_framework import routers

from .views import AgentViewSet

router = routers.DefaultRouter()
router.register("agent", AgentViewSet, "agent")

urlpatterns = [
    path('', include(router.urls))
]"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgentViewSet

router = DefaultRouter()
router.register(r'agents', AgentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]