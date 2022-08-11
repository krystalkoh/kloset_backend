from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AccountSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod ##this is static method ...don't need to create the instance
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email#adds on to the claims, not overwrite

        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class CustomTokenObtainPairSerializer (TokenObtainPairView)