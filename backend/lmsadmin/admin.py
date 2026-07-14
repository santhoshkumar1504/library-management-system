from django.contrib import admin
from .models import BookCategory, Author, Publisher, Book


@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_display_links = ['name']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    list_display_links = ['name']
    search_fields = ['name', 'email', 'phone']
    list_filter = ['name']
    ordering = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'isbn',
        'category',
        'authors',
        'publisher',
        'language',
        'published_year',
        'available_copies',
        'total_copies'
    ]

    list_display_links = ['title']

    search_fields = [
        'title',
        'isbn',
        'authors__name',
        'publisher__name',
        'category__name'
    ]

    list_filter = [
        'category',
        'authors',
        'publisher',
        'language',
        'published_year'
    ]

    ordering = ['title']

    readonly_fields = [
        'created_at',
        'updated_at'
    ]

    list_per_page = 20




admin.site.site_header = "Library Management System"
admin.site.site_title = "Library Admin"
admin.site.index_title = "Welcome to Library Dashboard"