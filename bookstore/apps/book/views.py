from .serializers import BookSerializer
from .models import Book
from rest_framework import generics
from rest_framework import mixins


class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        return self.list(request)

    def put(self, request):
        return self.update(request, id)
