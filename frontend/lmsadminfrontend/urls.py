from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='homeadmin'),

    path('books/', views.books, name='books'),

    path('categories/', views.categories, name='categories'),

    path('authors/', views.authors, name='authors'),

    path('publishers/', views.publishers, name='publishers'),

]