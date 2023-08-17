from rest_framework import generics
from ..models import Prihod
from ..serializers import PrihodSerializer

class PrihodList(generics.ListCreateAPIView):
    queryset = Prihod.objects.all()
    serializer_class = PrihodSerializer


class PrihodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Prihod.objects.all()
    serializer_class = PrihodSerializer