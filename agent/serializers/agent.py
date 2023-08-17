from rest_framework.serializers import ModelSerializer

from ..models import Agent


class AgentShortSerializer(ModelSerializer):

    class Meta:
        model = Agent
        fields = ["id", "clientname","address","clientphone"]


class AgentFullSerializer(ModelSerializer):

    parent = AgentShortSerializer()

    class Meta:
        model = Agent
        fields = ["id", "clientname","address","clientphone"]


class AgentChildsSerializer(ModelSerializer):

    subcategories = AgentShortSerializer(many=True)

    class Meta:
        model = Agent
        fields = ["id", "clientname","address","clientphone"]


class AgentCreateSerializer(ModelSerializer):

    class Meta:
        model = Agent
        fields = ["id", "clientname","address","clientphone"]
