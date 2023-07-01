from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status, viewsets


from Main.models import Category, Publication, Book, Author
from rest_framework.decorators import api_view
from .serializers import AuthorSerializer, PublicationSerializer, BookSerializer, CategorySerializer



# @api_view(['GET', 'POST', 'DELETE'])
# def book_list(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         books_serializer = BookSerializer(books, many = True)
#         return JsonResponse(books_serializer.data, safe=False,  json_dumps_params={'ensure_ascii': False})

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'
  
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
# Create your views here.
