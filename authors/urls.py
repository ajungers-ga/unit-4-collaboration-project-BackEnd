# File Purpose: This file defines the URL ROUTES for the AUTHORS APP.
#               These routes map incoming API requests to the correct view classes from authors/views.py.
#               These are the endpoints the frontend hits to list, create, or manage authors via /api/authors/


# 1. Imports
from django.urls import path         # Django’s function to define URL paths
from . import views                  # Importing the views from this app


# 2. URL Patterns
urlpatterns = [
    path('', views.AuthorListCreateView.as_view(), name='author_list'),         # Root path = handles GET/POST at /api/authors/
    path('<int:pk>/', views.AuthorRetrieveUpdateDestroyView.as_view(), name='author_detail'),  # Detail path = handles GET/PUT/PATCH/DELETE at /api/authors/<id>/
]

#---------------- NOTES BELOW ---------------#

# '' = ROOTPATH. Handles GET (list authors) and POST (create author)
# Example: /api/authors/

# <int:pk> = DETAILPATH. pk = primary key, int = ID of the author
# Handles GET/PUT/PATCH/DELETE requests for a specific author
# Example: /api/authors/5/ → returns or updates author with ID = 5

# These routes are scoped under /api/authors/ in config/urls.py
# This structure makes it easy for the frontend to fetch or manage author data using dynamic URLs
