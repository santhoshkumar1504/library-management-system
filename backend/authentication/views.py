from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserSerializer
from .models import Profile

@api_view(['GET','POST'])
def user(request):
    if request.method=='GET':
        profile_data=Profile.objects.all()
        data=UserSerializer(profile_data,many=True)
        return Response(data.data)
    if request.method=='POST':
        data=request.data
        des_data=UserSerializer(data=data)
        if des_data.is_valid():
            des_data.save()
            return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_200_OK)