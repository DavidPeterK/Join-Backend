from rest_framework import generics
from auth_user_app.models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from django.middleware.csrf import get_token


class UserProfileList(generics.ListCreateAPIView):
    """
    API view for listing all user profiles and creating a new user profile.
    Inherits from ListCreateAPIView to provide GET and POST methods.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, or deleting a specific user profile.
    Inherits from RetrieveUpdateDestroyAPIView to provide GET, PUT, PATCH, and DELETE methods.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class RegistrationView(APIView):
    """
    API view for user registration.
    Handles user creation and returns an authentication token upon successful registration.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Handles POST requests for user registration.
        Validates the data and creates a new user if valid, otherwise returns errors.
        """
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            saved_account = serializer.save()
            token, created = Token.objects.get_or_create(user=saved_account)
            data = {
                'token': token.key,
                'username': saved_account.username,
                'email': saved_account.email
            }
        else:
            data = serializer.errors
        return Response(data)


class CustomLoginView(ObtainAuthToken):
    """
    API view for user login.
    Extends ObtainAuthToken to return a token, username, email, and CSRF token upon successful login.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Handles POST requests for user login.
        Authenticates the user and returns a token along with user details and a CSRF token.
        """
        serializer = self.serializer_class(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            csrf_token = get_token(request)
            data = {
                'token': token.key,
                'username': user.username,
                'email': user.email,
                'csrfToken': csrf_token
            }
            return Response(data)
        else:
            data = serializer.errors
            return Response(data, status=406)
