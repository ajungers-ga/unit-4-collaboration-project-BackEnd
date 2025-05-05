# FILE PURPOSE = This file translates PYTHON model instances into JSON data. 
# The frontend can send and receive data in a readable format
# bonus nesting on the ReviewSerialzier


# 1. Import serializers and models
from rest_framework import serializers # impotring serialzers from DJANGO rest to build API translator
from .models import ReadingMaterial    # Importing the model/class(readingmaterial) that defines the data shape in the DB
from reviews.models import Review      # importing the Review model for nested serializer



# 2. Define ReviewSerializer for nested output
# BELOW = Define ReviewSerializer locally even though it also exists in the 'reviews' app.
# This avoids circular import issues and gives us control over how reviews appear when nested inside reading materials.
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'reviewer_name', 'comment', 'rating', 'created_at', 'reading_material']

# 3. Define ReadingMaterialSerializer
class ReadingMaterialSerializer(serializers.ModelSerializer):
    authorName = serializers.CharField()
    coverImage = serializers.URLField()
    publicationDate = serializers.DateField()
    isFeatured = serializers.BooleanField(default=False)
    isFavorite = serializers.BooleanField(default=False)
    readingStatus = serializers.CharField(default=None, allow_null=True) # allowing null to control the behavior of the field
    

    # Nested read-only reviews (reverse relation via related_name or default)
    reviews = ReviewSerializer(many=True, read_only=True)
    
# What is Meta class? Tells DJANGO what model to serialize and which fields to include (defined below)
    class Meta:
        model = ReadingMaterial
        fields = [
            'id',
            'title',
            'authorName',
            'coverImage',
            'publicationDate',
            'categories',
            'description',
            'type',
            'rating',
            'isFeatured',
            'isFavorite',
            'readingStatus',
            'created_at',
            'updated_at',
            'reviews'
        ]
