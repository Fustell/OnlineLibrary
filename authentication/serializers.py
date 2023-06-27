from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data["refreshToken"] = data["refresh"]
        data["accessToken"] = data["access"]
        del data["refresh"]
        del data["access"]

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
        return data