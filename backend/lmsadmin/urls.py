from django.urls import path
from .views import *


urlpatterns=[
    path('books/',books),

    # categories
    path('categories/',categories)
]