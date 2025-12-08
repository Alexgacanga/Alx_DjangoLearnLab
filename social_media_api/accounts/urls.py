from django.urls import path
from .views import RegisterView, ProfileView, FollowUserView, UnfollowUserView # Import new views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    
    # New endpoints for follow/unfollow
    path('follow/<int:pk>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:pk>/', UnfollowUserView.as_view(), name='unfollow_user'),
]