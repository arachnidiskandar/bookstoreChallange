from django.urls import  path
from .views import GenericAPIView, BookReserve

urlpatterns = [
    path('books/', GenericAPIView.as_view()),
    path('books/<int:id>/reserve/', BookReserve.as_view()),
]
