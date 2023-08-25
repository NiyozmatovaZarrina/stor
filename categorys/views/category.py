from rest_framework import generics
from categorys.models import Category
from categorys.serializers import CategorySerializer
from rest_framework import viewsets


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

