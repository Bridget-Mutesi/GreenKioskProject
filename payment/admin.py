from django.contrib import admin

# Register your models here.
from .models import Payment
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("amount","date_of_payment","pending_payment","receipt","payment_methods")
admin.site.register(Payment,PaymentAdmin)
