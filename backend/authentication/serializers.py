from rest_framework import serializers
from .models import Profile

class UserSerializer(serializers.Serializer):
    class Meta:
        model=Profile
        fields='__all__'