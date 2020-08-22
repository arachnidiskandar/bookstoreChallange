from .models import Client
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import ClientSerializer
from datetime import datetime
from rest_framework.renderers import JSONRenderer
import math


class ClientBooks(APIView):
    def get(self, request, id):
        try:
            client = Client.objects.get(id=id)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ClientSerializer(client)
        for book in serializer.data['borrowed_books']:
            days_borrowed = (datetime.today() - datetime.strptime(book['borrow_date'], '%Y-%m-%d')).days
            if days_borrowed > 3:
                price = float(book['borrow_price'])
                days_late = days_borrowed - 3
                if days_late <= 3:
                    penalty_value = (price * 0.03) + (price * pow(1.0002, days_late))
                elif days_late <= 5:
                    penalty_value = (price * 0.05) + (price * pow(1.0004, days_late))
                else:
                    penalty_value = (price * 0.07) + (price * pow(1.0006, days_late))
                book['delay_penalty_value'] = math.trunc(penalty_value * 100) / 100
        return Response(serializer.data)
