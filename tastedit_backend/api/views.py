# from django.shortcuts import render
from rest_framework import viewsets
from .models import Dish
from .serializers import DishSerializers

# Create your views here.
class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializers

