# File Purpose: This file defines the configuration settings for the AUTHORS APP.
#               Django uses this file to recognize, load, and initialize the app properly when the server starts.


# 1. Imports
from django.apps import AppConfig  # Django's built-in class to configure individual apps


# 2. Define AuthorsConfig
class AuthorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # default field type for auto-incrementing primary keys
    name = 'authors'  # name of the app as recognized by Django
