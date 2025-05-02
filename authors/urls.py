# authors/urls.py
from django.urls import path
from .views import AuthorListCreate, AuthorDetail

urlpatterns = [
    path('', AuthorListCreate.as_view(), name='author-list'),
    path('<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
]
