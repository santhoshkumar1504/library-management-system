from django.urls import path
from .views import *

urlpatterns=[

    #buy_book
    path('buy_book/',buy_book),
    
    # borrows
    path('borrows/',borrows),
    path('borrow/<int:id>',borrowBook),

    # Each copy Details
    path('bookcopy/',bookcopy),
    path('bookcopy/<int:id>',book),

    #Reserve the books
    path('reservedBooks/',reservedBooks),
    path('reservebook/<int:id>',reserveBook),

    #fine
    path('fines/',fines),
    path('fine/<int:id>',fine)

]