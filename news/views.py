from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import News
from .serializers import NewsSerializer

class NewsListCreateView(generics.ListCreateAPIView):
    queryset = News.objects.all().order_by('-date')
    serializer_class = NewsSerializer

class NewsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
