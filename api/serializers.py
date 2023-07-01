from rest_framework import serializers
from Main.models import Category, Publication, Book, Author



class BookSerializer(serializers.ModelSerializer):
    publication = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    author = serializers.StringRelatedField()
    
    class Meta:
        model = Book
        fields = '__all__'
        lookup_field = 'slug'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = '__all__'




class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication 
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'