from rest_framework import serializers
from ..models import Prihoddetail

class PrihoddetailSerializer(serializers.ModelSerializer):
    class Meta:
         model = Prihoddetail
         fields = ["id", "produktname","prihod","size","color","price"]

