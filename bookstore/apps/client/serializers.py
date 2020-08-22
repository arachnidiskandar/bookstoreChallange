from rest_framework import serializers
from .models import Client
from ..book.serializers import BookSerializer


class ClientSerializer(serializers.ModelSerializer):
    borrowed_books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'name', 'borrowed_books']
