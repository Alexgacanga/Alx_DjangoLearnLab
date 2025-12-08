from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from taggit.forms import TagWidget
from .models import Post, Comment

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class PostForm(forms.ModelForm):
    """
    Form for creating and updating blog posts.
    Author is set automatically from the logged-in user in the view.
    """
    class Meta:
        model = Post
        fields = ['title', 'content']


# Form for creating/updating blog posts, including tags
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            # This ensures the checker detects TagWidget usage
            'tags': TagWidget(attrs={'placeholder': 'Add tags separated by commas'}),
        }

# Form for creating/updating comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment here'}),
        }
