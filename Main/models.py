from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class Author(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Publication(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Book(models.Model): 
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name="author", on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, null=False, unique=True)
    category = models.ForeignKey(Category, related_name="category", on_delete=models.SET_NULL, null=True)
    publication = models.ForeignKey(Publication, related_name="publication", on_delete=models.SET_NULL, null=True)
    annotation = models.TextField()
    about = models.TextField()


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
