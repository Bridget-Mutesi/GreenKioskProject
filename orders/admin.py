from django.contrib import admin

# Register your models here.
from .models import Order
class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_Id","date_time","order_status","number_orders","total_amount","order_name")
admin.site.register(Order,OrderAdmin)
