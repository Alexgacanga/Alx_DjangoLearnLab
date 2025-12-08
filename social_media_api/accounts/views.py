from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import RegisterSerializer, UserSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer

# View for User Registration
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

# View for User Profile (Retrieve and Update)
class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Returns the currently authenticated user
        return self.request.user

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, user_id): # Changed pk to user_id
        user_to_follow = get_object_or_404(CustomUser, pk=user_id)
        
        if user_to_follow == request.user:
            return Response({"error": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(user_to_follow)
        return Response({"message": "Followed successfully"}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, user_id): # Changed pk to user_id
        user_to_unfollow = get_object_or_404(CustomUser, pk=user_id)
        
        request.user.following.remove(user_to_unfollow)
        return Response({"message": "Unfollowed successfully"}, status=status.HTTP_200_OK)