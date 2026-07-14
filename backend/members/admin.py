from django.contrib import admin

from .models import Reservation, BookCopy, Issued, FineModel


# Register your models here.
class ReservationAdmin(admin.ModelAdmin):
    list_display=['id','member','book','reservation_date','status']
    list_per_page=20
    list_display_links=['member']
    search_fields=['member','book']
    list_filter=['reservation_date']


class BookCopyAdmin(admin.ModelAdmin):
    list_display=['accession_number','book','status','price','shelf_location']
    list_display_links=['accession_number']
    search_fields=['book','accession_number']
    list_filter=['status','shelf_location']



@admin.register(Issued)
class IssuedAdmin(admin.ModelAdmin):
    list_display = [
        'member',
        'issueDate',
        'due_date',
        'return_date',
        'issued_by',
        'returned_by',
        'status'
    ]

    list_display_links = ['member']

    search_fields = [
        'member__username',
        'issued_by__username',
        'returned_by__username'
    ]

    list_filter = [
        'status',
        'issueDate',
        'due_date'
    ]

    ordering = ['-issueDate']


admin.site.register(Reservation,ReservationAdmin)

admin.site.register(BookCopy,BookCopyAdmin)

@admin.register(FineModel)
class FineModelAdmin(admin.ModelAdmin):
    list_display = [
        'member',
        'issue',
        'amount',
        'reason',
        'status',
        'waived_by',
        'created_at'
    ]

    list_display_links = ['member']

    search_fields = [
        'member__username',
        'issue__member__username',
        'reason',
        'status'
    ]

    list_filter = [
        'reason',
        'status',
        'created_at'
    ]

    ordering = ['-created_at']
