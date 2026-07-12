from django.db import models


class BookCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=150)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=150)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, unique=True)

    category = models.ForeignKey(
        BookCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name="books"
    )

    authors = models.ForeignKey(
    Author,
    on_delete=models.CASCADE,
    null=True
    )

    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.SET_NULL,
        null=True,
        related_name="books"
    )

    edition = models.CharField(max_length=50, blank=True)
    language = models.CharField(max_length=50, default="English")

    published_year = models.PositiveIntegerField()

    total_copies = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=1)

    shelf_number = models.CharField(max_length=20)

    cover_image = models.ImageField(
        upload_to="book_covers/",
        blank=True,
        null=True
    )

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
