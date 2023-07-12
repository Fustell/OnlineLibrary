from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView

from authentication.views import CustomTokenObtainPairView, LogoutView, ProfileView, CookieTokenRefreshView, \
    RegisterView

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
]