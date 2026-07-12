from django.urls import path
from .views import *


urlpatterns=[
    path('books/',books),

    # categories
    path('categories/',categories),
    path('category/<int:id>',category),

    path('authors/',authors),

    #publishers
    path('publishers/',publishers),
    path('publisher/<int:id>',publisher),
]