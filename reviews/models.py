from django.db import models
from reading_materials.models import ReadingMaterial

# Create your models here.
# 3. Define the model (Review)
class Review(models.Model):
    reading_material = models.ForeignKey(ReadingMaterial, on_delete=models.CASCADE, related_name='reviews')  # Connects review to a reading material
    reviewer_name = models.CharField(max_length=100)  # Could be replaced with a User model later
    comment = models.TextField()  # User comment
    rating = models.IntegerField()  # Individual review score (1–5)
    created_at = models.DateTimeField(auto_now_add=True)

# BELOW = # Dunder method (double underscore method).
# Django uses __str__ to control what gets displayed when the object is shown as text.
    def __str__(self):
        return f"Review by {self.reviewer_name} on {self.reading_material.title}"
