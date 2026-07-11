from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import BookCategorySerializer,AuthorSerializer, PublisherSerializer, BookSerializer
from  .models import Book, BookCategory, Author, Publisher

@api_view(['GET','POST'])
def books(request):
    if request.method=='GET':
        pass
    if request.method=='POST':
        book_data=request.data
        des_data=BookCategorySerializer(data=book_data)
        if des_data.is_valid():
            des_data.save()
            return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_200_OK)


@api_view(['GET','POST'])
def categories(request):
    if request.method=='GET':
        cdata=BookCategory.objects.all()
        data=BookCategorySerializer(cdata,many=True)
        return Response(data.data)
    if request.method=='POST':
        reqdata=request.data
        des_data=BookCategorySerializer(data=reqdata)
        if des_data.is_valid():
            des_data.save()
            return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_200_OK)


def category(request):
    pass