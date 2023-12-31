from django.db import models

# Create your models here.
class Notify(models.Model):
    sender_name = models.CharField(max_length = 32)
    title = models.CharField(max_length = 32)
    description = models.CharField(max_length = 32)
    message = models.TextField()
    time_date = models.DateTimeField()
    def __str__(self):
        return self.message
