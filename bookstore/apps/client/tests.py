from rest_framework.test import APITestCase, APIClient
from .models import Client
from ..book.models import Book
from django.urls import reverse
from rest_framework import status


class ClientViewTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.client_1 = Client.objects.create(name='Augusto')
        self.book_1 = Book.objects.create(name='Livro 1',
                                          status=Book.BookStatus.BORROWED,
                                          borrow_date='2020-08-22',
                                          borrow_price='10.0',
                                          borrowed_to=self.client)
        self.book_2 = Book.objects.create(name='Livro 2',
                                          status=Book.BookStatus.BORROWED,
                                          borrow_date='2020-08-19',
                                          borrow_price='10.0',
                                          borrowed_to=self.client)
    def test_penalty_property(self):
        res = self.client.get(reverse('client/<int:id>/books/', kwargs={'id': self.client_1.id}))
        print(res)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
