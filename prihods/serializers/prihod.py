from rest_framework.serializers import ModelSerializer

from ..models import Prihod


class PrihodShortSerializer(ModelSerializer):

    class Meta:
        model = Prihod
        fields = ["id", "provider","totalprice"]


class PrihodFullSerializer(ModelSerializer):

    parent = PrihodShortSerializer()

    class Meta:
        model = Prihod
        fields = ["id", "provider","totalprice"]


class PrihodChildsSerializer(ModelSerializer):

    subcategories = PrihodShortSerializer(many=True)

    class Meta:
        model = Prihod
        fields = ["id", "provider","totalprice"]


class PrihodCreateSerializer(ModelSerializer):

    class Meta:
        model = Prihod
        fields = ["id", "provider","totalprice"]
