# reading_materials/serializers.py

from rest_framework import serializers
from .models import ReadingMaterial

class ReadingMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingMaterial
        fields = '__all__'  # include all fields from ReadingMaterial
