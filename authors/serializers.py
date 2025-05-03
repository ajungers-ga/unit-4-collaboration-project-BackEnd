from rest_framework import serializers 
from .models import Author 

class AuthorSerializer(serializers.ModelSerializer):  # Converts model instances to JSON and vice versa
    class Meta:
        model = Author  # Specifies which model to serialize
        fields = ('id', 'name', 'photo', 'biography', 'popular_books')  # Fields to include in the JSON