from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

# Serializer for returning user info
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture']

# Serializer for registering a new user
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self, **kwargs):
        # Create user without directly calling create_user
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        # Hash the password properly
        user.set_password(self.validated_data['password'])
        user.save()
        # Create auth token
        Token.objects.create(user=user)
        return user

# Serializer for login (optional, token retrieval can also be handled in view)
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}
