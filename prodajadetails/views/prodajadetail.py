from rest_framework import generics
from ..models import Prodajadetail
from ..serializers import ProdajadetailSerializer

class ProdajadetailList(generics.ListCreateAPIView):
    queryset = Prodajadetail.objects.all()
    serializer_class = ProdajadetailSerializer


class ProdajadetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Prodajadetail.objects.all()
    serializer_class = ProdajadetailSerializer