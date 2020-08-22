from .serializers import BookSerializer
from .models import Book
from ..client.models import Client
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from rest_framework.views import APIView


class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get(self, request):
        return self.list(request)


class BookReserve(APIView):
    def put(self, request, id):
        updated_book = request.data
        try:
            book = Book.objects.get(id=id)
        except Exception as e:
            return Response('Book not Found', status=status.HTTP_404_NOT_FOUND)
        try:
            client = Client.objects.get(id=str(updated_book['borrowed_to']))
        except Exception as e:
            return Response('Client not Found', status=status.HTTP_404_NOT_FOUND)
        if not book.is_available():
            return Response('Book is already reserved', status=status.HTTP_400_BAD_REQUEST)
        if updated_book['status'] == Book.BookStatus.AVAILABLE:
            return Response('Book status invalid', status=status.HTTP_400_BAD_REQUEST)
        elif datetime.strptime(updated_book['borrow_date'], '%Y-%m-%d') > datetime.today():
            return Response('Borrow date invalid', status=status.HTTP_400_BAD_REQUEST)
        elif updated_book['description'] != book.description:
            return Response('Is not possible update the description', status=status.HTTP_400_BAD_REQUEST)
        elif updated_book['borrow_price'] != book.borrow_price:
            return Response('Is not possible update the borrow price', status=status.HTTP_400_BAD_REQUEST)
        elif updated_book['name'] != book.name:
            return Response('Is not possible update the book name', status=status.HTTP_400_BAD_REQUEST)
        serializer = BookSerializer(book, data=updated_book)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





