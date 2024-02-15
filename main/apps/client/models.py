from django.db import models
from ..common.models import BaseModel, BaseMeta

class Client(BaseModel):
    full_name = models.CharField(max_length=255)
    birthdate = models.DateField()


    class Meta(BaseMeta):
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
    
    def __str__(self):
        return f"{self.full_name}"