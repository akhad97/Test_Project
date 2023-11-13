from django.db.models import Sum, Count
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Client
from ..order.models import Order
    
class ClientStatisticsAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        month = self.request.query_params.get('month')
        year = self.request.query_params.get('year')
        orders = Order.objects.filter(client__id=pk, date__month=month, date__year=year)
        client = Client.objects.get(id=pk)

        data = {
            'number_of_products': orders.aggregate(total_products=Count('products__id'))['total_products'],
            'total_sales': orders.aggregate(total_sales=Sum('price'))['total_sales']
        }
        return Response(data)
    
client_statistics_api_view = ClientStatisticsAPIView.as_view()
    

    