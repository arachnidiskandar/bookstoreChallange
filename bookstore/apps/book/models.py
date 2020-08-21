from django.db import models


class Book(models.Model):
    class BookStatus(models.IntegerChoices):
        AVAILABLE = 1
        BORROWED = 2

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=BookStatus.choices, default=1)
    borrow_date = models.DateField(null=True, blank=True)
    borrow_value = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
