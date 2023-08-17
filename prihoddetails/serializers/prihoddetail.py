from rest_framework.serializers import ModelSerializer

from ..models import Prihoddetail


class PrihoddetailShortSerializer(ModelSerializer):

    class Meta:
        model = Prihoddetail
        fields = ["id", "produktname","prihod","size","color","price"]


class PrihoddetailFullSerializer(ModelSerializer):

    parent = PrihoddetailShortSerializer()

    class Meta:
        model = Prihoddetail
        fields = ["id", "produktname","prihod","size","color","price"]


class PrihoddetailChildsSerializer(ModelSerializer):

    subcategories = PrihoddetailShortSerializer(many=True)

    class Meta:
        model = Prihoddetail
        fields = ["id", "produktname","prihod","size","color","price"]


class PrihoddetailCreateSerializer(ModelSerializer):

    class Meta:
        model = Prihoddetail
        fields = ["id", "produktname","prihod","size","color","price"]
