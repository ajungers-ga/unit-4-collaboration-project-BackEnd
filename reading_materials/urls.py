# File Purpose: This file defines the IRL routes or endpoints specific to the reading_materials APP.
#               These routes map incoming API requests to the related VIEWS defined in reading_materials/ views.py
#               This is how Django knows how to behave/operate when a user visits  /api/reading-materials/


# 1. Imports
from django.urls import path
from .views import (
    ReadingMaterialListCreateView,
    ReadingMaterialRetrieveUpdateDestroyView,
)
# 2. URL Patterns
urlpatterns = [
    path('', ReadingMaterialListCreateView.as_view(), name='reading_material_list_create'),
    path('<int:pk>/', ReadingMaterialRetrieveUpdateDestroyView.as_view(), name='reading_material_detail'),
]

#---------------- NOTES BELOW ---------------#

# '' is the ROOTPATH. This handles the GET/POST reqs to /api/reading-materials/

# <int:pk = integer(datatype) and PRIMARY KEY which is the DETAILPATH...
# ... This handles GET/PUT/PATCH/DELETE for specific object

# EXAMPLE: say im at url /api/reading-materials/3/
# DJANGO will:
# match the url to <int:pk>
# pass pk=3 to the VIEW
# the VIEW will look up ReadingMaterial.objects.get(pk=3) under the hood
# the page displayed will be specific to the object ID of 3 under /api/reading-materials

# int:pk isnt the only coverter we can use. If we added AUTH for user signup...
# we could use <str:username> as a string like: /users/doctorjungers/
# or even
# <slug:slug> as a string: /books/harry-potter-and-the-chamber-of-secrets/ to see the details 