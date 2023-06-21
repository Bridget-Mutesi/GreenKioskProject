from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length = 32)
    email = models.CharField(max_length = 32)
    phone_number = models.CharField(max_length = 32)
    location = models.CharField(max_length =32)
    password = models.CharField(max_length = 32)
    def __str__(self):
        return self.user_name
