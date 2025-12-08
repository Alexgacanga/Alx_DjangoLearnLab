from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self, **kwargs):
        # Create user using User's own create_user method
        user = User.objects.create(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        user.set_password(self.validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
