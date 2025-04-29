# reading_materials/views.py

from rest_framework import generics
from .models import ReadingMaterial
from .serializers import ReadingMaterialSerializer

# List all Reading Materials or create a new one
class ReadingMaterialListCreateView(generics.ListCreateAPIView):
    queryset = ReadingMaterial.objects.all()
    serializer_class = ReadingMaterialSerializer

# Retrieve, update, or delete a specific Reading Material
class ReadingMaterialRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReadingMaterial.objects.all()
    serializer_class = ReadingMaterialSerializer
