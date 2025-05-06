# File Purpose: This file defines the ReviewSerialzer which translates Review MODEL instances to...
# ... and from JSON. Allows the frontend to send & receive REVIEW data in a format that works with REACT


# 1. Imports
from rest_framework import serializers # This lets me define how model data gets converted into JSON
from .models import Review             # The REVIEW MODEL (this is the data to be serialized)


# 2. Creating a serializer that AUTO maps ALL fields from the REVIEW MODEL using...
# ... DJANGO rest framework's ModelSerializer SHORTCUT
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'  # include all fields from Review


# Meta Class is telling DJANGO which MODEL the serialzier works with (Review) & ...
#          ... Which fields to include from that model. I have this set to ALL with DUNDER METHOD...
#           ... to have a better viewing experience from the ADMIN page