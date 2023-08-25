from rest_framework import generics
from agent.models import Agent
from agent.serializers import AgentSerializer
from rest_framework import viewsets


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer