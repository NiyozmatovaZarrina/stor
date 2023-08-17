from rest_framework.serializers import ModelSerializer

from ..models import Prodajadetail


class ProdajadetailShortSerializer(ModelSerializer):

    class Meta:
        model = Prodajadetail
        fields = ["id", "produktname","prodaja","size","color","price"]


class ProdajadetailFullSerializer(ModelSerializer):

    parent = ProdajadetailShortSerializer()

    class Meta:
        model = Prodajadetail
        fields = ["id", "produktname","prodaja","size","color","price"]


class ProdajadetailChildsSerializer(ModelSerializer):

    subcategories = ProdajadetailShortSerializer(many=True)

    class Meta:
        model = Prodajadetail
        fields = ["id", "produktname","prodaja","size","color","price"]


class ProdajadetailCreateSerializer(ModelSerializer):

    class Meta:
        model = Prodajadetail
        fields = ["id", "produktname","prodaja","size","color","price"]
