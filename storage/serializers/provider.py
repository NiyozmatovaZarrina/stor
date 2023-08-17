from rest_framework.serializers import ModelSerializer

from ..models import Provider


class ProviderShortSerializer(ModelSerializer):

    class Meta:
        model = Provider
        fields = ["id", "name","address","Phone_number","Email","Website","Activate"]


class ProviderFullSerializer(ModelSerializer):

    parent = ProviderShortSerializer()

    class Meta:
        model = Provider
        fields = ["id", "name","address","Phone_number","Email","Website","Activate"]


class ProviderChildsSerializer(ModelSerializer):

    subcategories = ProviderShortSerializer(many=True)

    class Meta:
        model = Provider
        fields = ["id", "name","address","Phone_number","Email","Website","Activate"]


class ProviderCreateSerializer(ModelSerializer):

    class Meta:
        model = Provider
        fields = ["id", "produktname","provider","category","size","color","price"]
