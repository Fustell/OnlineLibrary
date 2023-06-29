from django.contrib import admin
from django.urls import path


from django.conf.urls.static import static
from django.conf import settings

from .views import AuthorBookListView, AuthorListView, BookListView, CategoryListView, BookDetailView

urlpatterns = [
    path('', BookListView.as_view()),  # home page 
    path('authors/', AuthorListView.as_view()),  # authors list 
    path('authors/<slug:author_books>/', AuthorBookListView.as_view()),  # list  of books of one author
    path('categories/', CategoryListView.as_view()),  # categories list 
    path('<slug:book_slug>/', BookDetailView.as_view()),  # details of certain book
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)