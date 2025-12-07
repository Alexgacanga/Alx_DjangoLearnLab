from django.db import models
from django.utils import timezone

# -----------------------------
# Author Model
# -----------------------------
# This model stores basic information about an author.
# It has a one-to-many relationship with the Book model,
# since each author can write multiple books.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# -----------------------------
# Book Model
# -----------------------------
# This model stores book information and links each book
# to an Author via a ForeignKey. This establishes a
# one-to-many relationship (1 Author → Many Books).
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'  # Helps serializer include nested books
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
