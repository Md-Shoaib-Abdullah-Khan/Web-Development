from django.urls import path
from api.views import DogList, DogDetails, BreedList, BreedDetails
urlpatterns = [
    path('dogs/', DogList.as_view(), name='dog-list'),
    path('dogs/<int:pk>/', DogDetails.as_view(), name='dog-details'),
    path('breeds/', BreedList.as_view(), name='breed-list'),
    path('breeds/<int:pk>/', BreedDetails.as_view(), name='breed-details'),
]
