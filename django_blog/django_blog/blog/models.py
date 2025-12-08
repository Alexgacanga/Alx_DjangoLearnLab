from django.db import models
from django.contrib.auth.models import User

"""
Post Model
----------
Represents an individual blog post.

Fields:
    - title: The title of the blog post.
    - content: Main text body of the post.
    - published_date: Timestamp when the post was created.
    - author: ForeignKey to Django's User model.
"""

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title
