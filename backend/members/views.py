from django.shortcuts import render
from .models import Issued, Reservation, BookCopy, FineModel
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import IssuedSerializers, ReservationSerializers, FineSerializers, BookCopySerailizers
from lmsadmin.models import Book
from django.utils import timezone
from django.contrib.auth.models import User


@api_view(['POST','GET'])
def buy_book(request):
    try:
        if request.method=='POST':
            id=request.data
            user=id['uname']
            book=Book.objects.get(id=id['id'])
            cur_date=timezone.now()
            new=User.objects.get(username=user)
            try:
                exist=Reservation.objects.filter(member_id=new.id,book_id=book.id,expiry_date__lt=cur_date)
                if exist.exists():
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                    Reservation.objects.create(
                        book=book,
                        member=new,
                    )
                    book.available_copies=book.available_copies-1
                    book.save()
                    return Response(status=status.HTTP_201_CREATED)
            except:
               return Response(status=status.HTTP_401_UNAUTHORIZED) 
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)


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
    



@api_view(['POST'])
def reservedBooks(request):
    username = request.data.get('uname')
    if not username:
        return Response(
            {"error": "Username is required"},
            status=400
        )
    u = User.objects.filter(username=username).first()
    if not u:
        return Response(
            {"error": "User not found"},
            status=404
        )
    reservations = Reservation.objects.filter(member=u)
    serializer = ReservationSerializers(reservations, many=True)
    return Response(serializer.data)


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