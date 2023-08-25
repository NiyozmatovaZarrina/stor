from rest_framework import generics
from produkts.models import Produkt
from produkts.serializers import ProduktSerializer
from rest_framework import viewsets


class ProduktViewSet(viewsets.ModelViewSet):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer

