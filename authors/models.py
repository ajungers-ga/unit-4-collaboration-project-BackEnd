# FILE PURPOSE:
# This file defines the AUTHOR MODEL. This model stores structured information about authors who have written 
# books, manga, or magazines in our app. Each author has a name, photo, biography, and a list of their popular works.
# This keeps author data separate from reading materials, allowing for cleaner organization and reuse across books.

from django.db import models


# 1. Define the Author model
class Author(models.Model):
    name = models.CharField(max_length=255)  # Author's full name
    photo = models.URLField()                # IMG URL to represent the author's face or profile picture
    biography = models.TextField()           # Longer field for bio, background, or accomplishments
    popular_books = models.JSONField(default=list)  # Stores list of book IDs associated with this author

    # BELOW = Dunder method (double underscore method)
    # Controls how the object is displayed in the admin dashboard or terminal.
    # Instead of seeing "Author object (1)", you’ll see "J.K. Rowling" or "Matt Haig"
    def __str__(self):
        return self.name
