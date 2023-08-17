from rest_framework.serializers import ModelSerializer

from ..models import Prodaja


class ProdajaShortSerializer(ModelSerializer):

    class Meta:
        model = Prodaja
        fields = ["id", "provider","totalprice"]


class ProdajaFullSerializer(ModelSerializer):

    parent = ProdajaShortSerializer()

    class Meta:
        model = Prodaja
        fields = ["id", "username"," productname"," agentname","totalprice"]


class ProdajaChildsSerializer(ModelSerializer):

    subcategories = ProdajaShortSerializer(many=True)

    class Meta:
        model = Prodaja
        fields = ["id", "username"," productname"," agentname","totalprice"]


class ProdajaCreateSerializer(ModelSerializer):

    class Meta:
        model = Prodaja
        fields = ["id", "username"," productname"," agentname","totalprice"]
