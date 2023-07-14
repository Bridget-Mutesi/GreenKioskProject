from django.db import models
from  django.contrib.auth.models import User

# Create your models here.

class Order(models.Model):
    payment = models.oneToOneField(User, on_delete = models.PROTECT, null = True)
    order_name = models.CharField(max_length = 32, default='Default Order Name')
    order_Id = models.CharField(max_length = 32)
    date_time = models.DateTimeField()
    order_status = models.CharField(max_length = 32)
    number_orders = models.IntegerField()
    total_amount = models.IntegerField()
    def __str__(self):
        return self.order_name

