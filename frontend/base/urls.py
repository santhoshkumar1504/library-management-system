from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('detail/<int:id>',details,name='details'),
    path('catelog/',catelog,name='catelog')
]