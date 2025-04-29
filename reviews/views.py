# reviews/views.py

from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer

# List all Reviews or create a new one
class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Retrieve, update, or delete a specific Review
class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
