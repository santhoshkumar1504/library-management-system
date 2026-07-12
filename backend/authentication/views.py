from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from .models import Profile
from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    ProfileSerializer,
    ChangePasswordSerializer,
    ForgotPasswordSerializer,
    ResetPasswordSerializer,
)

@api_view(['POST','GET'])
def register(request):

    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(
            {
                "message": "Registration Successful"
            },
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST','GET'])
def login(request):

    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:

            refresh = RefreshToken.for_user(user)

            return Response({

                "message": "Login Successful",

                "refresh": str(refresh),

                "access": str(refresh.access_token)

            })

        return Response({

            "error": "Invalid Username or Password"

        }, status=status.HTTP_401_UNAUTHORIZED)

    return Response(serializer.errors)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):

    return Response({

        "message": "Logout Successful"

    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):

    profile = Profile.objects.get(user=request.user)

    serializer = ProfileSerializer(profile)

    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request):

    profile = Profile.objects.get(user=request.user)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    serializer = ProfileSerializer(
        profile,
        data=request.data,
        partial=True
    )

    if serializer.is_valid():
        serializer.save()

        return Response({
            "message": "Profile Updated Successfully",
            "data": serializer.data
        })

    return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):

    serializer = ChangePasswordSerializer(
        data=request.data
    )

    if serializer.is_valid():

        if not request.user.check_password(
                serializer.validated_data['old_password']):

            return Response({

                "error": "Old Password is Incorrect"

            })

        request.user.set_password(
            serializer.validated_data['new_password']
        )

        request.user.save()

        return Response({

            "message": "Password Changed Successfully"

        })

    return Response(serializer.errors)

@api_view(['POST'])
def forgot_password(request):

    serializer = ForgotPasswordSerializer(
        data=request.data
    )

    if serializer.is_valid():

        email = serializer.validated_data['email']

        if User.objects.filter(email=email).exists():

            return Response({

                "message": "Email Found. Reset your password."

            })

        return Response({

            "error": "Email Not Found"

        })

    return Response(serializer.errors)

@api_view(['POST'])
def reset_password(request):

    serializer = ResetPasswordSerializer(
        data=request.data
    )

    if serializer.is_valid():

        username = serializer.validated_data['username']
        new_password = serializer.validated_data['new_password']

        try:

            user = User.objects.get(username=username)

            user.set_password(new_password)

            user.save()

            return Response({

                "message": "Password Reset Successfully"

            })

        except User.DoesNotExist:

            return Response({

                "error": "User Not Found"

            })

    return Response(serializer.errors)