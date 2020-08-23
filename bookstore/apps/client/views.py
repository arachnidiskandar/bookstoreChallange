from .models import Client
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import ClientSerializer
from datetime import datetime
from rest_framework.renderers import JSONRenderer
import math


class ClientBooks(APIView):
    def get_delay_penalty_value(self, interest, days_late, borrow_price, fixed_percentage_value):
        return (borrow_price * (fixed_percentage_value / 100)) + (borrow_price * pow((1 + interest / 100), days_late))

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
                    penalty_value = (self.get_delay_penalty_value(0.2, days_late, price, 3) - price)
                elif days_late <= 5:
                    penalty_value = (self.get_delay_penalty_value(0.4, days_late, price, 5) - price)
                else:
                    penalty_value = (self.get_delay_penalty_value(0.6, days_late, price, 7) - price)
                book['delay_penalty_value'] = (math.trunc(penalty_value * 100) / 100)
        return Response(serializer.data)
