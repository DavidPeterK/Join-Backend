from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import generics
from auth_user_app.models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import ValidationError


class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
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
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,
                'username': user.username,
                'email': user.email
            }
        else:
            data = serializer.errors

        return Response(data)


@api_view(['GET'])
def validate_email(request):
    email = request.query_params.get('email')
    if not email:
        return Response({"error": "Email parameter is required"}, status=400)
    try:
        if User.objects.filter(email=email).exists():
            raise ValidationError(
                "Ein Benutzer mit dieser E-Mail-Adresse existiert bereits.")
        return Response({"valid": True})
    except ValidationError as e:
        return Response({"valid": False, "error": str(e)})


@api_view(['GET'])
def validate_username(request):
    username = request.query_params.get('username')
    try:
        if User.objects.filter(username=username).exists():
            raise ValidationError(
                "Ein Benutzer mit diesem Benutzernamen existiert bereits.")
        return Response({"valid": True})
    except ValidationError as e:
        return Response({"valid": False, "error": str(e)})


@api_view(['POST'])
def validate_passwords(request):
    password = request.data.get('password')
    repeated_password = request.data.get('repeated_password')
    if not password or not repeated_password:
        return Response({"error": "Password and repeated_password are required"}, status=400)
    try:
        if password != repeated_password:
            raise ValidationError("Die Passwörter stimmen nicht überein.")
        return Response({"valid": True})
    except ValidationError as e:
        return Response({"valid": False, "error": str(e)})
