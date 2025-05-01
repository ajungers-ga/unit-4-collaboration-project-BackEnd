# models.py

# 1. Import Django's model base class
from django.db import models

# 2. Define the model (ReadingMaterial)
class ReadingMaterial(models.Model):
    title = models.CharField(max_length=255)  # Short text field (e.g., "Harry Potter")
    author_name = models.CharField(max_length=255)  # Short text field (e.g., "J.K. Rowling")
    cover_image = models.URLField(blank=True) # IMG URL placeholder
    publication_date = models.DateField(null=True, blank=True)
    categories = models.JSONField(default=list)
    description = models.TextField()  # Long text field (e.g., summary of the book)
    type = models.CharField(max_length=100)  # Type of reading material (e.g., Book, Magazine, Manga)
    rating = models.FloatField(default=0.0)  # Optional: backend can update this later based on review ratings
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when updated

# BELOW = # Dunder method (double underscore method).
# Django uses __str__ to control what gets displayed when the object is shown as text.
# This improves the Admin view — instead of showing 'Company object (1)', it shows a readable name like 'Apple' or 'Google'.
    def __str__(self):
        return self.title