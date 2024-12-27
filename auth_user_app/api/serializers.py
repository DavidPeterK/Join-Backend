from rest_framework import serializers
from auth_user_app.models import UserProfile
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the UserProfile model.
    Includes user, bio, and location fields.
    """

    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'location']


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    Includes username, email, password, and repeated_password fields.
    """
    repeated_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeated_password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def save(self):
        """
        Validates and creates a new user account.
        Ensures passwords match and email/username are unique.
        """
        pw = self.validated_data['password']
        repeated_pw = self.validated_data['repeated_password']
        if pw != repeated_pw:
            raise serializers.ValidationError({
                'error': 'passwords dont match'
            })
        self._validate_unique_user()
        return self._create_user(pw)

    def _validate_unique_user(self):
        """
        Validates that email and username are unique.
        Raises ValidationError if duplicates exist.
        """
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({
                'error': 'User with that email already exists'
            })
        if User.objects.filter(username=self.validated_data['username']).exists():
            raise serializers.ValidationError({
                'error': 'User with that username already exists'
            })

    def _create_user(self, password):
        """
        Creates and saves a new user with hashed password.
        Returns the created user instance.
        """
        account = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        account.set_password(password)
        account.save()
        return account
