from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod ##this is static method ...don't need to create the instance
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email#adds on to the claims, not overwrite

        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

