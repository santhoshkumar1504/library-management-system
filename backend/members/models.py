from django.db import models
from lmsadmin.models import Book
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone

# Borrowed or Returned, user, date, increment/decrement (in Book model)
class BookCopy(models.Model):
    statusChoices=(
        ('Available','Available'),
        ('Borrowed','Borrowed'),
        ('Reserved','Reserved'),
        ('Lost','Lost'),
        ('Damaged','Damaged')
    )
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    accession_number=models.CharField(max_length=50,unique=True)
    status=models.CharField(max_length=50,choices=statusChoices,default='Available')
    price=models.FloatField()
    shelf_location=models.CharField(max_length=40)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



def get_expiration_date():
    return timezone.now()+timedelta(days=14)


class Issued(models.Model):
    bookChoices=(
        ('Issued','Issued'),
        ('Returned','Returned'),
        ('Overdue','Overdue')
    )
    member=models.ForeignKey(User,on_delete=models.CASCADE, related_name="issues")
    issueDate=models.DateTimeField(default=timezone.now)
    due_date=models.DateTimeField(default=get_expiration_date)
    return_date=models.DateTimeField()
    issued_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name="issued_books")
    returned_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name="returned_books")
    status=models.CharField(max_length=30,choices=bookChoices)
    remarks=models.TextField(max_length=50,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Reservation(models.Model):
    reserveChoices=(
        ('Pending','Pending'),
        ('Ready','Ready'),
        ('Cancelled','Cancelled'),
        ('Expired','Expired')
    )
    member=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    reservation_date=models.DateTimeField(default=timezone.now)
    expiry_date=models.DateTimeField(default=get_expiration_date)
    fulfilled_date=models.DateTimeField(null=True)
    status=models.CharField(max_length=50,default='Pending')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



class FineModel(models.Model):
    fineReason=(
        ('Late Return','Late Return'),
        ('Lost Book','Lost Book'),
        ('Damage','Damage')
    )
    fineStatus=(
        ('Pending','Pending'),
        ('Paid','Paid'),
        ('Waived','Waived')
    )
    issue=models.OneToOneField(Issued,on_delete=models.CASCADE)
    member=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    reason=models.CharField(max_length=30,choices=fineReason)
    status=models.CharField(max_length=30,choices=fineStatus)
    waived_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name="waived_fines",null=True)
    remarks=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)