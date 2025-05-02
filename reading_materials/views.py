# reading_materials/views.py

from rest_framework import generics
from .models import ReadingMaterial, Author
from .serializers import ReadingMaterialSerializer, AuthorSerializer

# Reading Material Views
class ReadingMaterialListCreateView(generics.ListCreateAPIView):
    queryset = ReadingMaterial.objects.all()
    serializer_class = ReadingMaterialSerializer

class ReadingMaterialRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReadingMaterial.objects.all()
    serializer_class = ReadingMaterialSerializer

# Author Views
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
