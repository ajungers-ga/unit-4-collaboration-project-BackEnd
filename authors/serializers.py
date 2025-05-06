# File Purpose: This file defines the AuthorSerializer which translates AUTHOR MODEL instances to...
# ... and from JSON. Allows the frontend to send & receive AUTHOR data in a readable format (especially in REACT).


# 1. Imports
from rest_framework import serializers        # This lets us define how model data gets converted into JSON
from .models import Author                     # The AUTHOR MODEL — this is the data being serialized


# 2. Creating a serializer that AUTO maps fields from the AUTHOR MODEL using...
# ... Django REST Framework’s ModelSerializer shortcut
class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author  # Specifies which model this serializer works with (Author)
        fields = ('id', 'name', 'photo', 'biography', 'popular_books')  # Fields we want to include in the JSON output


# Meta class = tells Django which MODEL to serialize and which FIELDS to include
# This allows REACT (or another frontend) to send and receive author data in a structured format
# These fields match the ones defined in the Author model inside authors/models.py
