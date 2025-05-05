# File Purpose: This file defines our API views for lising and CRUD using th DJANGO REST Framework
#               These VIEWS connect the MODELS/SERIALIZERS to API endpoints on the front, so they can CALL using...
#           ... FETCH or AXIOS

# 1. Imports
from rest_framework import generics # generics uses DRF views that handle API ops, w/o writing them f/ scratch
from .models import ReadingMaterial # ReadingMaterial is the MODEL we're EXPOSING through API
from .serializers import ReadingMaterialSerializer # this serializer converts MODEL instances to & f/ JSON for req/res

# 2. ReadingMaterialListCreateView
# BELOW = the handling of listing GET/Post 
class ReadingMaterialListCreateView(generics.ListCreateAPIView):
    queryset = ReadingMaterial.objects.all() # query set is the data SOURCE. all(ReadingMaterials) entries in the DB
    serializer_class = ReadingMaterialSerializer # DRF uses serializer_class to convert MODEL to & f/ JSON


# 3. ReadingMaterialRetrieveUpdateDestroyView
# BELOW = the handling of GET/PUT/DELETE from /api/reading-materials/<id>/
# This class gives the full CRUD control for individual reading materials using the primary key of <id>
class ReadingMaterialRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReadingMaterial.objects.all()
    serializer_class = ReadingMaterialSerializer

# These views tie into our URLs and the front team can connect them using fetch calls to...
# /api/reading-materials/<id>/      OR     /api/reading-materials/:id