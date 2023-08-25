from rest_framework import generics
from prihoddetails.models import Prihoddetail
from prihoddetails.serializers import PrihoddetailSerializer
from rest_framework import viewsets


class PrihoddetailViewSet(viewsets.ModelViewSet):
    queryset = Prihoddetail.objects.all()
    serializer_class = PrihoddetailSerializer

