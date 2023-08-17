from rest_framework import generics
from ..models import Prodaja
from ..serializers import ProdajaSerializer

class ProdajaList(generics.ListCreateAPIView):
    queryset = Prodaja.objects.all()
    serializer_class = PrihodSerializer


class ProdajaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Prodaja.objects.all()
    serializer_class = ProdajaSerializer