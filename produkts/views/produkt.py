from rest_framework import generics
from ..models import Produkt
from ..serializers import ProduktSerializer

class ProduktList(generics.ListCreateAPIView):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer


class ProduktDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Produkt.objects.all()
    serializer_class = ProduktSerializer