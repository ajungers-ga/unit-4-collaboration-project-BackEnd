# reading_materials/views.py

from rest_framework import generics
from .models import ReadingMaterial
from .serializers import ReadingMaterialSerializer

# Reading Material Views
class ReadingMaterialListCreateView(generics.ListCreateAPIView):
    queryset = ReadingMaterial.objects.all()
    serializer_class = ReadingMaterialSerializer

class ReadingMaterialRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReadingMaterial.objects.all()
    serializer_class = ReadingMaterialSerializer

