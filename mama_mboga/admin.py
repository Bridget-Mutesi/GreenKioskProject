from django.contrib import admin

# Register your models here.
from .models import Mboga
class MbogaAdmin(admin.ModelAdmin):
    list_display = ("name_mboga","email_address","number","location_mboga","password_mboga")
admin.site.register(Mboga,MbogaAdmin)
