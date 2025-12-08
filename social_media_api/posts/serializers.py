from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    # Nested serializer to show comments inside the post (optional, but helpful)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'comments', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']