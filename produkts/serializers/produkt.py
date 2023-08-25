from rest_framework import serializers
from ..models import Produkt

class ProduktSerializer(serializers.ModelSerializer):
    class Meta:
         model = Produkt
         fields = ["id", "produktname","provider","category","size","color","price"]

  