from rest_framework import serializers
from .models import Issued, BookCopy,Reservation,FineModel

class IssuedSerializers(serializers.Serializer):
    class Meta:
        model=Issued
        fields='__all__'


class BookCopySerailizers(serializers.Serializer):
    class Meta:
        model=BookCopy
        fields='__all__'


class ReservationSerializers(serializers.Serializer):
    class Meta:
        model=Reservation
        fields='__all__'


class FineSerializers(serializers.Serializer):
    class Meta:
        model=FineModel
        fields='__all__'