from rest_framework import serializers
from django.utils import timezone
from .models import Author, Book


# --------------------------------------------
# Book Serializer
# --------------------------------------------
# This serializer handles the Book model.
# It also includes custom validation to ensure
# publication_year is never in the future.
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation to prevent future publication years
    def validate_publication_year(self, value):
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


# --------------------------------------------
# Author Serializer (with Nested Books)
# --------------------------------------------
# This serializer includes a nested representation
# of books belonging to an author.
#
# The 'books' field uses the BookSerializer for each
# related Book model instance. This automatically
# serializes nested relationships using the 'related_name'
# defined in the Book model.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
