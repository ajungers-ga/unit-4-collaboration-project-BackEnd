from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    photo = models.URLField()  # URL to the author's photo
    biography = models.TextField()
    popular_books = models.JSONField(default=list)  # List of book IDs

    def __str__(self):
        return self.name