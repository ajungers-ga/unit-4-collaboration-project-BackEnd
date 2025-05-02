# FILE PURPOSE:
# This file defines Django models related to user-generated reviews and authors.
# It includes the Review model (linked to reading materials) and the Author model (linked to books by ID).

from django.db import models
from reading_materials.models import ReadingMaterial

# 1. Define the Review model
class Review(models.Model):
    reading_material = models.ForeignKey(ReadingMaterial, on_delete=models.CASCADE, related_name='reviews')  # Connects review to a reading material
    reviewer_name = models.CharField(max_length=100)  # Could be replaced with a User model later
    comment = models.TextField()  # User comment
    rating = models.IntegerField()  # Individual review score (1–5)
    created_at = models.DateTimeField(auto_now_add=True)

    # Controls how this object is displayed (in admin panel and shell)
    def __str__(self):
        return f"Review by {self.reviewer_name} on {self.reading_material.title}"

