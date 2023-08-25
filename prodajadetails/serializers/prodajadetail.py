from rest_framework import serializers
from ..models import Prodajadetail

class ProdajadetailSerializer(serializers.ModelSerializer):
    class Meta:
         model = Prodajadetail
         fields = ["id", "produktname","prodaja","size","color","price"]