from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    photo = models.URLField()  # Image URL
    biography = models.TextField()
    popular_books = models.JSONField(default=list)  # List of book IDs

    def __str__(self):
        return self.name
