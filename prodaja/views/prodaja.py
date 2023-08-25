from rest_framework import generics
from prodaja.models import Prodaja
from prodaja.serializers import ProdajaSerializer
from rest_framework import viewsets


class ProdajaViewSet(viewsets.ModelViewSet):
    queryset = Prodaja.objects.all()
    serializer_class = ProdajaSerializer

