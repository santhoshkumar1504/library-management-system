from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET','POST'])
def books(request):
    if request.method=='GET':
        pass
    if request.method=='POST':
        book_data=request.data
        des_data=BookSerializers(data=book_data)
        if des_data.is_valid():
            des_data.save()
            return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_200_OK)-