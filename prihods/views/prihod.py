from rest_framework import generics
from prihods.models import Prihod
from prihods.serializers import PrihodSerializer
from rest_framework import viewsets


class PrihodViewSet(viewsets.ModelViewSet):
    queryset = Prihod.objects.all()
    serializer_class = PrihodSerializer

