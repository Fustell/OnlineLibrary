from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from autoslug import AutoSlugField


class Author(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Publication(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name

def book_upload_location(instance, filename):
    filebase, extension = filename.split('.')
    return 'title_books/%s.%s' % (instance.slug, extension)


class Book(models.Model): 
    title = models.CharField(max_length=100)
    title_photo = models.ImageField(upload_to='title_photos/')
    book = models.FileField()
    author = models.ForeignKey(Author, related_name="author", on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, null=False, unique=True)
    category = models.ForeignKey(Category, related_name="category", on_delete=models.SET_NULL, null=True)
    publication = models.ForeignKey(Publication, related_name="publication", on_delete=models.SET_NULL, null=True)
    annotation = models.TextField()
    about = models.TextField()
    year_release = models.IntegerField(null=True)
    is_released = models.BooleanField()
    
    def __str__(self):
        return self.title

