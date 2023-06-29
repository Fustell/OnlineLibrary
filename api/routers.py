from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'books', views.BookViewSet,basename="book")
router.register(r'categories', views.CategoryViewSet, basename="category")
router.register(r'authors', views.AuthorViewSet, basename="author")
router.register(r'publications', views.PublicationViewSet, basename="publication")

# router.register(r'users', views.UserViewSet,basename="user")