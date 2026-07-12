from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password'
        ]

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Email already exists."
            )
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                "Username already exists."
            )
        return value

    def create(self, validated_data):

        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        return user

class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()

    password = serializers.CharField(
        write_only=True
    )

class ProfileSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(
        source='user.first_name'
    )

    last_name = serializers.CharField(
        source='user.last_name'
    )

    username = serializers.CharField(
        source='user.username',
        read_only=True
    )

    email = serializers.EmailField(
        source='user.email'
    )

    class Meta:
        model = Profile

        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
            'city',
            'state',
            'pincode',
            'profile_image'
        ]

    def update(self, instance, validated_data):

        user_data = validated_data.pop('user', {})

        user = instance.user

        user.first_name = user_data.get(
            'first_name',
            user.first_name
        )

        user.last_name = user_data.get(
            'last_name',
            user.last_name
        )

        user.email = user_data.get(
            'email',
            user.email
        )

        user.save()

        instance.phone = validated_data.get(
            'phone',
            instance.phone
        )

        instance.address = validated_data.get(
            'address',
            instance.address
        )

        instance.city = validated_data.get(
            'city',
            instance.city
        )

        instance.state = validated_data.get(
            'state',
            instance.state
        )

        instance.pincode = validated_data.get(
            'pincode',
            instance.pincode
        )

        if validated_data.get('profile_image'):
            instance.profile_image = validated_data.get(
                'profile_image'
            )

        instance.save()

        return instance

class ChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField()

    new_password = serializers.CharField(
        min_length=8
    )

class ForgotPasswordSerializer(serializers.Serializer):

    email = serializers.EmailField()

class ResetPasswordSerializer(serializers.Serializer):

    username = serializers.CharField()

    new_password = serializers.CharField(
        min_length=8
    )