from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm


def register_view(request):
    """
    Custom user registration view.
    Uses extended UserCreationForm (with email).
    """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Auto-login user after registration
            login(request, user)
            return redirect("profile")
    else:
        form = RegisterForm()

    return render(request, "blog/register.html", {"form": form})


@login_required
def profile_view(request):
    """
    Allows authenticated users to view and update profile details.
    """
    if request.method == "POST":
        user = request.user
        user.email = request.POST.get("email")
        user.save()
        return render(request, "blog/profile.html", {
            "user": user,
            "message": "Profile updated successfully!"
        })

    return render(request, "blog/profile.html", {"user": request.user})
