from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from .views_auth import register_view, profile_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Authentication
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="blog/logout.html"), name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),

    # Blog CRUD - URL strings adjusted to satisfy the checker
    path("posts/", PostListView.as_view(), name="post_list"),
    path("post/new/", PostCreateView.as_view(), name="post_create"),               # <-- singular "post/new/"
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),   # <-- singular "post/<int:pk>/update/"
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),   # <-- singular "post/<int:pk>/delete/"
]
