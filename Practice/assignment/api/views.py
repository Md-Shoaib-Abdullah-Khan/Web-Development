from django.shortcuts import render
from rest_framework import generics
from api.models import Dog, Breed
from api.serializers import DogSerializer, BreedSerializer
# Create your views here.
class BreedList(generics.ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

class BreedDetails(generics.RetrieveUpdateDestroyAPIView):
     queryset = Breed.objects.all()
     serializer_class = BreedSerializer

class DogList(generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class DogDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer