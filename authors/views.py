from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import AuthorSerializer
from .models import Author

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer
class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer