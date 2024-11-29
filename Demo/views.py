from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .serializers import UserProfileSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAdmin, IsUser, IsModerator, IsAuthenticated, AllowAny


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializers = UserProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        })
    return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdmin])
def admin_home(request):
    content = {"message": "Welcome Admin"}
    return Response(content, status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsUser])
def user_home(request):
    content = {"message": "Welcome User"}
    return Response(content, status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsModerator])
def moderator_home(request):
    content = {"message": "Welcome Moderator"}
    return Response(content, status=200)
