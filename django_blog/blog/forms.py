from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


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
