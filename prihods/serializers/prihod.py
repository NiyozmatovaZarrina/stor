from rest_framework import serializers
from ..models import Prihod

class PrihodSerializer(serializers.ModelSerializer):
    class Meta:
         model = Prihod
         fields = ["id", "user","totalprice"]



