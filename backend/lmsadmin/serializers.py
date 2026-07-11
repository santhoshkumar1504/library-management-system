from rest_framework import serializers
from .models import BookCategory,Author,Publisher,Book

class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=BookCategory
        fields="__all__"
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'
    
class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Publisher
        fields='__all__'

class BookSerializer(serializers.ModelSerializer):

    category=BookCategorySerializer(read_only=True)
    authors=AuthorSerializer(read_only=True)
    publisher=PublisherSerializer(read_only=True)

    class Meta:
        model=Book
        fields='__all__'