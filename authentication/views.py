from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.serializers import CustomTokenObtainPairSerializer, CookieTokenRefreshSerializer


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        data = {
            "username": "Roman",
            "email": "koplimrom@gmail.com",
            "Role": "admin"
        }

        return Response(data, status=status.HTTP_200_OK)


class LogoutView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            refresh_token = request.COOKIES.get("refresh_token")
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def finalize_response(self, request, response, *args, **kwargs):
        response.delete_cookie('refresh_token')
        return super().finalize_response(request, response, *args, **kwargs)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh'):
            cookie_max_age = 3600 * 24 * 14  # 14 days
            response.set_cookie('refresh_token', response.data['refresh'], max_age=cookie_max_age, httponly=False)
            # del response.data['refresh']
        return super().finalize_response(request, response, *args, **kwargs)


class CookieTokenRefreshView(TokenRefreshView):
    serializer_class = CookieTokenRefreshSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh'):
            cookie_max_age = 3600 * 24 * 14  # 14 days
            response.set_cookie('refresh_token', response.data['refresh'], max_age=cookie_max_age, httponly=False)
            # del response.data['refresh']
        return super().finalize_response(request, response, *args, **kwargs)