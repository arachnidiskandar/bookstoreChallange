from rest_framework import  serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'description', 'status', 'borrow_date', 'borrow_price']
