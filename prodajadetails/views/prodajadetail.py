from rest_framework import generics
from prodajadetails.models import Prodajadetail
from prodajadetails.serializers import ProdajadetailSerializer
from rest_framework import viewsets


class ProdajadetailViewSet(viewsets.ModelViewSet):
    queryset = Prodajadetail.objects.all()
    serializer_class = ProdajadetailSerializer

