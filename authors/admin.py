# File Purpose: This file registers the Author model to the Django Admin dashboard.
# This allows the backend team to add, edit, or delete authors using a visual interface.


# 1. Imports
from django.contrib import admin  # gives us access to Django's admin interface
from .models import Author        # importing the Author model from this app


# 2. Register Author model
admin.site.register(Author)  # makes Author appear in the Django admin panel under localhost:8000/admin/


# admin is the MODULE
# site is the variable for AdminSite