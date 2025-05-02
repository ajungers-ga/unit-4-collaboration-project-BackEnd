# reading_materials/urls.py

from django.urls import path
from .views import (
    ReadingMaterialListCreateView,
    ReadingMaterialRetrieveUpdateDestroyView,
    AuthorListCreateView
)

urlpatterns = [
    path('', ReadingMaterialListCreateView.as_view(), name='reading_material_list_create'),
    path('<int:pk>/', ReadingMaterialRetrieveUpdateDestroyView.as_view(), name='reading_material_detail'),
    path('authors/', AuthorListCreateView.as_view(), name='author_list_create'),
]
