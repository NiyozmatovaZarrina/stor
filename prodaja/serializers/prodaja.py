from rest_framework import serializers
from ..models import Prodaja

class ProdajaSerializer(serializers.ModelSerializer):
    class Meta:
         model = Prodaja
         fields = ["id", "username","productname","agentname","totalprice"]

