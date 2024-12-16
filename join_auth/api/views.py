from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserRegistrationSerializer, UserProfileSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from join_auth.models import UserProfile


class UserRegistrationAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = CustomUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
              'message': 'User registered successfully',
              'token': token.key,  
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "message": "Login successful"
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "error": "Invalid email or password"
            }, status=status.HTTP_401_UNAUTHORIZED)


class UserProfileListAPIView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        profile = request.user.profile  
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data, status=200)
    
class UserProfileDetailView(APIView):
    def get(self, request, pk, format=None):
        user_profile = UserProfile.objects.get(pk=pk)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        user_profile = UserProfile.objects.get(pk=pk)
        serializer = UserProfileSerializer(user_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

