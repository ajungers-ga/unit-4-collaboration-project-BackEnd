# File Purpose: This file defines the API views for the REVIEWS APP. These views handle the logic for...
#               Listing, creating, retrieving, updating, and deleting user reviews through HTTP requests.
#               These views connect the REVIEW MODEL/SERIALIZER to API endpoints the frontend can call using FETCH or AXIOS.


# 1. Imports 
from rest_framework import generics  # DRF's generic class based views that save us f/ rewriting CRUD logic from scratch
from .models import Review           # Import the REVIEW MODEL to expose its data through the API
from .serializers import ReviewSerializer  # This serializer converts Review instances to/from JSON


# 2. ReviewListCreateView
# BELOW = Handles GET (list all reviews) and POST (create a new review) at /api/reviews/
class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()              # Data source: all Review entries in the DB
    serializer_class = ReviewSerializer          # Serializer used to convert Reviews <--> JSON


# 3. ReviewRetrieveUpdateDestroyView
# BELOW = Handles GET, PUT, PATCH, DELETE for an individual review using its <id> (primary key)
# This gives full CRUD control for a single review at /api/reviews/<id>/
class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
