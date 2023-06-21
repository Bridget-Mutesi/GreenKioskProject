from django.contrib import admin

# Register your models here.
from .models import User
class UserAdmin(admin.ModelAdmin):
    list_display = ("user_name","email","phone_number","location","password")
admin.site.register(User,UserAdmin)
