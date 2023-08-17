from rest_framework.serializers import ModelSerializer

from ..models import Produkt


class ProdajadetailShortSerializer(ModelSerializer):

    class Meta:
        model = Produkt
        fields = ["id", "produktname","prodaja","size","color","price"]


class ProduktFullSerializer(ModelSerializer):

    parent = ProduktShortSerializer()

    class Meta:
        model = Produkt
        fields = ["id", "produktname","provider","category","size","color","price"]


class ProduktChildsSerializer(ModelSerializer):

    subcategories = ProduktShortSerializer(many=True)

    class Meta:
        model = Produkt
        fields = ["id", "produktname","provider","category","size","color","price"]


class ProduktCreateSerializer(ModelSerializer):

    class Meta:
        model = Produkt
        fields = ["id", "produktname","provider","category","size","color","price"]
