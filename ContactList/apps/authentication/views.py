from rest_framework.generics import GenericAPIView
from .serializers.serializers import UserSerializer, LoginSerializer
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterAPIView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            serializer = UserSerializer(user)
            refresh = RefreshToken.for_user(user=user)
            return Response({'user': serializer.data,
                            'access': str(refresh.access_token)}, status=status.HTTP_200_OK)
        return Response({
            'message': 'Incorrect username or password'
        }, status=status.HTTP_401_UNAUTHORIZED)
