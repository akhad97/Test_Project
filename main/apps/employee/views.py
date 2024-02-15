from rest_framework.views import APIView
from django.db.models import Sum, Count
from rest_framework.response import Response
from ..order.models import Order
from .models import Employee


class EmployeeStatisticsAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        month = self.request.query_params.get('month')
        year = self.request.query_params.get('year')
        orders = Order.objects.filter(employee__id=pk, date__month=month, date__year=year)
        employee = Employee.objects.get(id=pk)
        data = {
            'full_name': employee.full_name,
            'number_of_clients': orders.values('client').distinct().count(), 
            'number_of_products': orders.aggregate(total_products=Count('products__id'))['total_products'],
            'total_sales': orders.aggregate(total_sales=Sum('price'))['total_sales']
        }
        return Response(data)

employee_statistics_api_view = EmployeeStatisticsAPIView.as_view()
    

class AllEmployeeStatisticsAPIView(APIView):
    def get(self, *args, **kwargs):
        month = self.request.query_params.get('month')
        year = self.request.query_params.get('year')
        employees = Employee.objects.all()
        statistics_list = []
        for employee in employees:
            orders = Order.objects.filter(employee=employee, date__month=month, date__year=year)
            data = {
                'employee_id': employee.id,
                'full_name': employee.full_name,
                'number_of_clients': orders.values('client').distinct().count(), 
                'number_of_products': orders.aggregate(total_products=Count('products__id'))['total_products'],
                'total_sales': orders.aggregate(total_sales=Sum('price'))['total_sales']
            }
            statistics_list.append(data)
        return Response(statistics_list)

all_employee_statistics_api_view = AllEmployeeStatisticsAPIView.as_view()
