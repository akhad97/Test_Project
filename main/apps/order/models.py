from django.db import models
from ..common.models import BaseModel, BaseMeta
from ..client.models import Client
from ..employee.models import Employee
from ..product.models import Product


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()


    class Meta(BaseMeta):
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
    
    def __str__(self):
        return f"{self.client.full_name}"