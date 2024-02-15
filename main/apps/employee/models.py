from django.db import models
from ..common.models import BaseModel, BaseMeta



class Employee(BaseModel):
    full_name = models.CharField(max_length=255)
    birthdate = models.DateField()

    class Meta(BaseMeta):
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
    
    def __str__(self):
        return f"{self.full_name}"