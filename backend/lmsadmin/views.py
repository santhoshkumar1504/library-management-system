from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Author
from .serializers import AuthorSerializer


@api_view(['GET', 'POST'])
def auther(request):

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