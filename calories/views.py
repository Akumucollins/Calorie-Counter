from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from .serializers import *
from rest_framework import viewsets, permissions

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
class FooditemView(viewsets.ModelViewSet):
    queryset = Fooditem.objects.all()
    serializer_class = FooditemSerializer
    
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class UserFooditemView(viewsets.ModelViewSet):
    queryset = UserFooditem.objects.all()
    serializer_class = UserFooditemSerializer                