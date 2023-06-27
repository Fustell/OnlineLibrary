from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from authentication.serializers import CustomTokenObtainPairSerializer

class LogoutView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
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
        if response.data.get('refreshToken'):
            cookie_max_age = 3600 * 24 * 14  # 14 days
            response.set_cookie('refresh_token', response.data['refreshToken'], max_age=cookie_max_age, httponly=False)
            del response.data['refreshToken']
        return super().finalize_response(request, response, *args, **kwargs)