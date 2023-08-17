from rest_framework.serializers import ModelSerializer

from ..models import User


class UserShortSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "name","address","Phone_number","Email","Website","Activate"]


class UserFullSerializer(ModelSerializer):

    parent = UserShortSerializer()

    class Meta:
        model = User
        fields = ["id", "name","address","Phone_number","Email","Website","Activate"]


class UserChildsSerializer(ModelSerializer):

    subcategories = UserShortSerializer(many=True)

    class Meta:
        model = User
        fields = ["id", "name","address","Phone_number","Email","Website","Activate"]


class UserCreateSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "produktname","provider","category","size","color","price"]
