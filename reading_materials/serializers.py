# reading_materials/serializers.py

# 1. Import serializers and models
from rest_framework import serializers
from .models import ReadingMaterial
from reviews.models import Review  # Import Review model

# 2. Define ReviewSerializer for nested use
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'reviewer_name', 'comment', 'rating', 'created_at', 'reading_material']

# 3. Define ReadingMaterialSerializer
class ReadingMaterialSerializer(serializers.ModelSerializer):
    # BELOW = # Pull in all related reviews automatically, read-only so frontend can't create them here
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = ReadingMaterial
        fields = '__all__'  # Include all fields from ReadingMaterial, plus the new 'reviews' field
