# FILE PURPOSE:
# This file defines the REVIEW MODEL. This model stores USER feedback for each reading material. 
# This is connected to the ReadingMaterial Model through a foreign key(Line11) which is allowing us to...
# ... group MULTIPLE reviews under a SINGLE book/magazine/manga. Creating a one to many relationship

from django.db import models
from reading_materials.models import ReadingMaterial

# 1. Define the Review model
class Review(models.Model):
    reading_material = models.ForeignKey(ReadingMaterial, on_delete=models.CASCADE, related_name='reviews')  # Connects review to a reading material
    reviewer_name = models.CharField(max_length=100)  # Could be replaced with a User model later
    comment = models.TextField()  # User comment
    rating = models.IntegerField()  # Individual review score (1–10)
    created_at = models.DateTimeField(auto_now_add=True)

   # BELOW = # Dunder method (double underscore method).
# Django uses __str__ to control what gets displayed when the object is shown as text.
# This improves the Admin view — instead of showing 'Company object (1)', it shows a readable name like 'Apple' or 'Google'.
    def __str__(self):
        return f"Review by {self.reviewer_name} on {self.reading_material.title}"


# line 11: on_delete=models.CASCADE = if the reading material is deleted, its reviews are also deleted
# line 11: related_name='reviews') = Gives access to ALL reviews of a specific book
