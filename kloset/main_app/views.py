from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ClothesSerializer
from .serializers import UsersSerializer
from .models import Clothes
from .models import Users
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class UsersList(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def get(self, request, *args, **kwargs):
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        users_serializer = UsersSerializer(data=request.data)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response(users_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', users_serializer.errors)
            return Response(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClothesList(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)
    def get(self, request, *args, **kwargs):
        clothes = Clothes.objects.all()
        serializer = ClothesSerializer(clothes, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        clothes_serializer = ClothesSerializer(data=request.data)
        if clothes_serializer.is_valid():
            clothes_serializer.save()
            return Response(clothes_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', clothes_serializer.errors)
            return Response(clothes_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JwtDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        response = JWTAuthentication().authenticate(request)
        if response is not None:
            account, token = response

            print(account)
            print(account.id)
            print(account.given_name)
            print(account.other_name)

            return Response(token.payload)

        return Response('error')
