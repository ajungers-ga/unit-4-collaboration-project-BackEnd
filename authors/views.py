# File Purpose: This file defines the API VIEWS for the AUTHORS APP.
# These views handle the logic for listing, creating, retrieving, updating, and deleting authors.
# They connect the AUTHOR MODEL and SERIALIZER to real API endpoints that the frontend can call using FETCH or AXIOS.


# 1. Imports
from django.shortcuts import render           # Required for completeness, not used in API views
from rest_framework import generics           # DRF generics help us quickly set up full CRUD functionality
from .serializers import AuthorSerializer     # Handles JSON translation of Author data
from .models import Author                    # The Author model is what we expose through the API


# 2. AuthorListCreateView
# BELOW = Handles GET (list all authors) and POST (create a new author) at /api/authors/
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all().order_by('id')   # Pulls all authors from the DB, ordered by ID
    serializer_class = AuthorSerializer          # Uses the serializer to convert between Author & JSON


# 3. AuthorRetrieveUpdateDestroyView
# BELOW = Handles GET, PUT/PATCH, and DELETE for a specific author at /api/authors/<id>/
class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all().order_by('id')   # Queryset for targeting one author by primary key
    serializer_class = AuthorSerializer
