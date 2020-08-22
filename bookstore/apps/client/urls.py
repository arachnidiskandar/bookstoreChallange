from django.urls import path
from .views import ClientBooks

urlpatterns = [
    path('client/<int:id>/books/', ClientBooks.as_view()),
]