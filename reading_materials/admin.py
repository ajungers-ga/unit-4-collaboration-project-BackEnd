from django.contrib import admin
from .models import ReadingMaterial

admin.site.register(ReadingMaterial)


# ABOVE = The registration of the model(ReadingMaterial) so it shows up in the DJANGO admin panel...
#     ... for easier inspection and editing    

# admin is the MODULE
# site is the variable for AdminSite