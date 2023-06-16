from django.contrib import admin
from .models import  Author, Category, Publication, Book


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publication)
admin.site.register(Category)

# Register your models here.
