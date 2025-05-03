# reading_materials/urls.py

from django.urls import path
from .views import (
    ReadingMaterialListCreateView,
    ReadingMaterialRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('', ReadingMaterialListCreateView.as_view(), name='reading_material_list_create'),
    path('<int:pk>/', ReadingMaterialRetrieveUpdateDestroyView.as_view(), name='reading_material_detail'),
]
