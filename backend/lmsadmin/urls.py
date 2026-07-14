from django.urls import path
from .views import *


urlpatterns=[
    # books
    path('books/',books),
    path('book/<int:id>',book),

    # for searching
    path('search/<name>',search),
    path('similarbooks/<int:id>',bookByCateogory),

    # categories
    path('categories/',categories),
    path('category/<int:id>',category),

    # author
    path('authors/',authors),
    path('author/<int:id>',author),

    # publishers
    path('publishers/',publishers),
    path('publisher/<int:id>',publisher),
]