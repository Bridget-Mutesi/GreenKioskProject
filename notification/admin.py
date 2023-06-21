from django.contrib import admin

# Register your models here.
from .models import Notify
class NotifyAdmin(admin.ModelAdmin):
    list_display = ("sender_name","title","description","message","time_date")
admin.site.register(Notify,NotifyAdmin)
