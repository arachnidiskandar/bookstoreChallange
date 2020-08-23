from django.urls import  path
from .views import GetAllBooks, BookReserve

urlpatterns = [
    path('books/', GetAllBooks.as_view()),
    path('books/<int:id>/reserve/', BookReserve.as_view()),
]
