from django.db import models
from ..client.models import Client


class Book(models.Model):
    class BookStatus(models.TextChoices):
        AVAILABLE = 'Available'
        BORROWED = 'Borrowed'

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=9, choices=BookStatus.choices, default=BookStatus.AVAILABLE)
    borrow_date = models.DateField(null=True, blank=True)
    borrow_price = models.DecimalField(max_digits=8, decimal_places=2)
    borrowed_to = models.ForeignKey(Client,
                                    related_name='borrowed_books',
                                    on_delete=models.CASCADE,
                                    null=True,
                                    blank=True)

    def __str__(self):
        return self.name
