# File Purpose: This file registers the REVIEW MODEL with the DJANGO admin site so we can view, 
# add, edit, or delete reviews from the browser based admin dashboard


# 1. Imports
from django.contrib import admin # Importing DJANGOS built in ADMIN tools
from .models import Review       # Importing the REVIEW model f/ the current App

# 2. Registration
admin.site.register(Review)      # This tells DJANGO to include Review model in admin UI
                                 # Once registered, we can see  the "Reviews" section at http://localhost:8000/admin/
