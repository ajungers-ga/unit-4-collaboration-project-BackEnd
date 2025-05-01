# # reading_materials/serializers.py

# # 1. Import serializers and models
# from rest_framework import serializers
# from .models import ReadingMaterial
# from reviews.models import Review  # Import Review model

# # 2. Define ReviewSerializer for nested use
# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = ['id', 'reviewer_name', 'comment', 'rating', 'created_at', 'reading_material']

# # 3. Define ReadingMaterialSerializer
# class ReadingMaterialSerializer(serializers.ModelSerializer):
#     # BELOW = # Pull in all related reviews automatically, read-only so frontend can't create them here
#     reviews = ReviewSerializer(many=True, read_only=True)

#     class Meta:
#         model = ReadingMaterial
#         fields = '__all__'  # Include all fields from ReadingMaterial, plus the new 'reviews' field








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
    # Map snake_case model fields to camelCase keys for the frontend
    authorName = serializers.CharField(source='author_name')
    coverImage = serializers.URLField(source='cover_image')
    publicationDate = serializers.DateField(source='publication_date')
    isFeatured = serializers.BooleanField(default=False)
    isFavorite = serializers.BooleanField(default=False)
    readingStatus = serializers.CharField(default=None, allow_null=True)
    
    # Nested read-only reviews
    reviews = ReviewSerializer(many=True, read_only=True)

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
            'average_score',
            'isFeatured',
            'isFavorite',
            'readingStatus',
            'created_at',
            'updated_at',
            'reviews'
        ]
