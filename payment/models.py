from django.db import models

# Create your models here.
class Payment(models.Model):
    amount = models.IntegerField()
    date_of_payment = models.DateField()
    pending_payment = models.BooleanField()
    receipt = models.CharField(max_length=32)
    payment_methods = models.CharField(max_length=32)
    def __str__(self):
        return self.receipt
