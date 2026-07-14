from rest_framework import serializers
from .models import Issued, BookCopy,Reservation,FineModel
from lmsadmin.serializers import BookSerializer

class IssuedSerializers(serializers.ModelSerializer):
    class Meta:
        model=Issued
        fields='__all__'


class BookCopySerailizers(serializers.ModelSerializer):
    class Meta:
        model=BookCopy
        fields='__all__'


class ReservationSerializers(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    class Meta:
        model=Reservation
        fields='__all__'


class FineSerializers(serializers.ModelSerializer):
    class Meta:
        model=FineModel
        fields='__all__'