from django.db import models
from lmsadmin.models import Book
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone

# Borrowed or Returned, user, date, increment/decrement (in Book model)
class BookCopy(models.Model):
    class stausChoices(models.TextChoices):
        c1="Available","Available"
        c2="Borrowed","Borrowed"
        c3="Reserved","Reserved"
        c4="Lost","Lost"
        c5="Damaged","Damaged"
    
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    accession_number=models.CharField(max_length=50,unique=True)
    status=models.CharField(max_length=50,choices=stausChoices.choices,default='Available')
    price=models.FloatField()
    shelf_location=models.CharField(max_length=40)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.accession_number



def get_expiration_date():
    return timezone.now()+timedelta(days=30)


class Issued(models.Model):
    class bookChoices(models.TextChoices):
        c1="","Select Option"
        c2="Issued","Issued"
        c3="Returned","Returned"
        c4="Overdue","Overdue"
    member=models.ForeignKey(User,on_delete=models.CASCADE, related_name="issues")
    issueDate=models.DateTimeField(default=timezone.now)
    due_date=models.DateTimeField(default=get_expiration_date)
    return_date=models.DateTimeField()
    issued_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name="issued_books")
    returned_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name="returned_books")
    status=models.CharField(max_length=30,choices=bookChoices.choices)
    remarks=models.TextField(max_length=50,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



class Reservation(models.Model):
    class ReserveChoices(models.TextChoices):
        SELECT = "", "Select Option"
        PENDING = "Pending", "Pending"
        BORROWED = "Borrowed", "Borrowed"
        READY = "Ready", "Ready"
        CANCELLED = "Cancelled", "Cancelled"
        EXPIRED = "Expired", "Expired"
    member=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    reservation_date=models.DateTimeField(default=timezone.now)
    expiry_date=models.DateTimeField(default=get_expiration_date)
    fulfilled_date=models.DateTimeField(null=True)
    status=models.CharField(max_length=50,default='Pending',choices=ReserveChoices.choices)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('member', 'book')



class FineModel(models.Model):
    class FineReason(models.TextChoices):
        SELECT = "", "Select Option"
        LATE_RETURN = "Late Return", "Late Return"
        LOST_BOOK = "Lost Book", "Lost Book"
        DAMAGE = "Damage", "Damage"

    class FineStatus(models.TextChoices):
        SELECT = "", "Select Option"
        PENDING = "Pending", "Pending"
        PAID = "Paid", "Paid"
        WAIVED = "Waived", "Waived"
    issue=models.OneToOneField(Issued,on_delete=models.CASCADE)
    member=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    reason=models.CharField(max_length=30,choices=FineReason.choices)
    status=models.CharField(max_length=30,choices=FineStatus.choices)
    waived_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name="waived_fines",null=True)
    remarks=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)