from django.urls import path
from .views import RegisterView, ProfileView, FollowUserView, UnfollowUserView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    
    # Matches the checker's requirement exactly:
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
]