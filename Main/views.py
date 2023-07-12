from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Book, Author, Category
from django.shortcuts import get_object_or_404

# list of authors
class AuthorListView(ListView):
    model = Author
    template_name = 'Main/author_list.html'
    context_object_name = 'authors'


# list of books
class BookListView(ListView):
    model = Book
    template_name = 'Main/book_list.html'
    context_object_name = 'books'


# details of one book
class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    slug_url_kwarg = 'book_slug'
    

# list of categories
class CategoryListView(ListView):
    model = Category 
    template_name = 'Main/categories_list.html'
    context_object_name = 'categories'
