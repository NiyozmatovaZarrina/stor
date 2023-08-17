from rest_framework import generics
from ..models import Prihoddetail
from ..serializers import PrihoddetailSerializer

class PrihoddetailList(generics.ListCreateAPIView):
    queryset = Prihoddetail.objects.all()
    serializer_class = PrihoddetailSerializer


class PrihoddetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prihoddetail.objects.all()
    serializer_class = PrihoddetailSerializer