from django.db import models
from ..common.models import BaseModel, BaseMeta



class Product(BaseModel):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


    class Meta(BaseMeta):
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return f"{self.name}"