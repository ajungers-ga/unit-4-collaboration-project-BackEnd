from rest_framework import generics
from .models import Author
from .serializers import AuthorSerializer

class AuthorListCreate(generics.ListCreateAPIView):
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer
