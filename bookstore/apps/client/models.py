from django.db import models
from ..book.models import Book


class Client(models.Model):
    name = models.CharField(max_length=100)
    borrowed_books = models.ManyToManyField(Book, null=True, blank=True)

    def __str__(self):
        return self.name
