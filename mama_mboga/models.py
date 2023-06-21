from django.db import models

# Create your models here.
class Mboga(models.Model):
    name_mboga = models.CharField(max_length = 32)
    email_address = models.CharField(max_length = 32)
    number = models.CharField(max_length = 32)
    location_mboga = models.CharField(max_length = 32)
    password_mboga = models.CharField(max_length = 32)
    def __str__(self):
        return self.name_mboga
    