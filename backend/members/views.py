from django.shortcuts import render
from .models import Issued, Reservation, BookCopy, FineModel
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import IssuedSerializers, ReservationSerializers, FineSerializers, BookCopySerailizers

@api_view(['GET','POST'])
def borrows(request):
    if request.method=='GET':
        bookdata=Issued.objects.filter(member=request.user)
        res=IssuedSerializers(bookdata,many=True)
        return Response(res.data)
    if request.method=='POST':
        fine=FineModel.objects.filter(member=request.user)
        if len(fine)==0:
            data=request.data
            des=IssuedSerializers(data=data)
            if des.is_valid():
                des.save()
                return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_208_ALREADY_REPORTED)
    return Response(status=status.HTTP_102_PROCESSING)


@api_view(['GET','DELETE','PUT'])
def borrowBook(request,id):
    model_data=Issued.objects.get(id=id)
    if request.method=='GET':
        res=IssuedSerializers(model_data)
        return Response(res.data)
    elif request.method=='PUT':
        data=request.data
        des=IssuedSerializers(instance=model_data,data=data)
        if des.is_valid():
            des.save()
            return Response(status=status.HTTP_202_ACCEPTED)
    elif request.method=='DELETE':
        model_data.delete()
        return Response(status=status.HTTP_410_GONE)
    


@api_view(['GET','POST'])
def bookcopy(request):
    if request.method=='GET':
        books=BookCopy.objects.all()
        json=BookCopySerailizers(books,many=True)
        return Response(json.data)
    if request.method=='POST':
        data=request.data
        des=BookCopySerailizers(data=data)
        if des.is_valid():
            des.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        

@api_view(['GET','PUT','DELETE'])
def book(request,id):
    model_data=BookCopy.objects.get(id=id)
    if request.method=='GET':
        jsondata=BookCopySerailizers(model_data)
        return Response(jsondata.data)
    if request.method=='PUT':
        data=request.data
        des=BookCopySerailizers(instance=model_data,data=data)
        if des.is_valid():
            des.save()
            return Response(status=status.HTTP_200_OK)
    if request.method=='DELETE':
        model_data.delete()
        return Response(status=status.HTTP_410_GONE)
    



@api_view(['GET','POST'])
def reservedBooks(request):
    if request.method=='GET':
        data=Reservation.objects.filter(member=request.user)
        des=ReservationSerializers(data,many=True)
        return Response(des.data)
    if request.method=='POST':
        newReserve=request.data
        des=ReservationSerializers(data=newReserve)
        if des.is_valid():
            des.save()
            return Response(status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def reserveBook(request,id):
    model_data=Reservation.objects.get(id=id)
    if request.method=='GET':
        jsondt=ReservationSerializers(model_data)
        return Response(jsondt.data)
    if request.method=='PUT':
        data=request.data
        des=ReservationSerializers(instance=model_data,data=data)
        if des.is_valid():
            des.save()
            return Response(status=status.HTTP_200_OK)
    if request.method=='DELETE':
        model_data.delete()
        return Response(status=status.HTTP_410_GONE)
    



@api_view(['GET','POST'])
def fines(request):
    if request.method=='GET':
        data=FineModel.objects.filter(member=request.user)
        des=FineSerializers(data,many=True)
        return Response(des.data)
    if request.method=='POST':
        newReserve=request.data
        des=FineSerializers(data=newReserve)
        if des.is_valid():
            des.save()
            return Response(status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def fine(request,id):
    model_data=FineModel.objects.get(id=id)
    if request.method=='GET':
        jsondt=FineSerializers(model_data)
        return Response(jsondt.data)
    if request.method=='PUT':
        data=request.data
        des=FineSerializers(instance=model_data,data=data)
        if des.is_valid():
            des.save()
            return Response(status=status.HTTP_200_OK)
    if request.method=='DELETE':
        model_data.delete()
        return Response(status=status.HTTP_410_GONE)