from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import BookCategorySerializer,AuthorSerializer, PublisherSerializer, BookSerializer
from  .models import Book, BookCategory, Author, Publisher
from django.db.models import Q




@api_view(['GET','POST'])
def books(request):
    if request.method=='GET':
        bookdata=Book.objects.all()
        bdata=BookSerializer(bookdata,many=True)
        return Response(bdata.data)
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



@api_view(['GET','DELETE','PUT'])
def category(request,id):
    model_data=get_object_or_404(BookCategory,id=id)
    if request.method=='GET':
        category=BookCategorySerializer(model_data)
        return Response(category.data)
    
    elif request.method=='PUT':
        catdata=request.data
        des_data=BookCategorySerializer(instance=model_data,data=catdata)
        if des_data.is_valid():
            des_data.save()
            return Response(status=status.HTTP_202_ACCEPTED,data='Data Updated')
    elif request.method=='DELETE':
        model_data.delete()
        return Response(status=status.HTTP_410_GONE)
    return Response(status=status.HTTP_200_OK)



@api_view(['GET','POST'])
def publishers(request):
    if request.method=='GET':
        data=Publisher.objects.all()
        json_data=PublisherSerializer(data, many=True)
        return Response(json_data.data)
    if request.method=='POST':
        newdata=request.data
        des_data=PublisherSerializer(newdata)
        if des_data.is_valid():
            des_data.save()
            return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_200_OK)


@api_view(['GET','PUT','DELETE'])
def publisher(request,id):
    model_data=get_object_or_404(Publisher,id=id)
    if request.method=='GET':
        data=PublisherSerializer(model_data)
        return Response(data.data)
    if request.method=='PUT':
        newdata=request.data
        des=PublisherSerializer(instance=model_data,data=newdata)
        if des.is_valid():
            des.save()
            return Response(status=status.HTTP_202_ACCEPTED)
    if request.method=='DELETE':
        model_data.delete()
        return Response(status=status.HTTP_410_GONE)
    return Response(status=status.HTTP_200_OK)





@api_view(['GET', 'POST'])
def authors(request):

    if request.method == 'GET':
        auth_data = Author.objects.all()
        auth_ser = AuthorSerializer(auth_data, many=True)
        return Response(auth_ser.data)


    if request.method == "POST":
        req_data = request.data
        auth_ser = AuthorSerializer(data=req_data)

        if auth_ser.is_valid():
            auth_ser.save()
            return Response(auth_ser.data, status=status.HTTP_201_CREATED)

        return Response(auth_ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def book(request,id):
    model_data=get_object_or_404(Book,id=id)
    if request.method=='GET':
        res=BookSerializer(model_data)
        return Response(res.data)
    if request.method=='PUT':
        data=request.data
        res=BookSerializer(instance=model_data,data=data)
        if res.is_valid():
            res.save()
            return Response(status=status.HTTP_202_ACCEPTED)
    if request.method=='DELETE':
        model_data.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def search(request,name):
    if request.method=='GET':
        data=Book.objects.filter(title__icontains=name)
        json_data=BookSerializer(data,many=True)
        return Response(json_data.data)
    return Response(status=status.HTTP_200_OK)








@api_view(['GET','PUT','DELETE'])
def author(request,id):
    model_data=get_object_or_404(Author,id=id)
    if request.method=='GET':
        jsondata=AuthorSerializer(model_data)
        return Response(jsondata.data)
    if request.method=='PUT':
        data=request.data
        des=AuthorSerializer(instance=model_data,data=data)
        if des.is_valid():
            des.save()
            return Response(status=status.HTTP_202_ACCEPTED)
    if request.method=='DELETE':
        model_data.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_200_OK)
    