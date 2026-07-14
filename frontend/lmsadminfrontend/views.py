from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render


BASE_URL = "http://127.0.0.1:8000/api/"


def home(request):
    return render(request, "homeadmin.html")


def books(request):

    response = requests.get("http://127.0.0.1:8000/api/books/")

    books = []

    if response.status_code == 200:
        books = response.json()

    print(books)   # <-- Add this line

    return render(request, "books.html", {
        "books": books
    })


def categories(request):

    response = requests.get(BASE_URL + "categories/")

    categories = []

    if response.status_code == 200:
        categories = response.json()

    return render(request, "categories.html", {
        "categories": categories
    })


def authors(request):

    response = requests.get(BASE_URL + "authors/")

    authors = []

    if response.status_code == 200:
        authors = response.json()

    return render(request, "authors.html", {
        "authors": authors
    })


def publishers(request):

    response = requests.get(BASE_URL + "publishers/")

    publishers = []

    if response.status_code == 200:
        publishers = response.json()

    return render(request, "publishers.html", {
        "publishers": publishers
    })