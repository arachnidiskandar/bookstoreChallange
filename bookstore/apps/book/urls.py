from django.urls import  path
from .views import GenericAPIView

urlpatterns = [
    path('books/', GenericAPIView.as_view()),
]
