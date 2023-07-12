from django.contrib.auth.models import User
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.serializers import CustomTokenObtainPairSerializer, CookieTokenRefreshSerializer, \
    RegisterSerializer, UserSerializer


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        user = User.objects.get(id=request.auth.payload["user_id"])
        data = {
            "username": user.username,
            "email": user.email,
            "role": "admin"if user.is_superuser else "moderator" if user.is_stuff else "user"
        }

        return Response(data, status=status.HTTP_200_OK)

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


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