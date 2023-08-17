from django.urls import path, include
from rest_framework import routers

from .views import AgentViewSet

router = routers.DefaultRouter()
router.register("agent", AgentViewSet, "agent")

urlpatterns = [
    path('', include(router.urls))
]
