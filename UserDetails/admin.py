from django.contrib import admin
from .models import User_details, User_Address

@admin.register(User_details)
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number')
    search_fields = ('id', 'name', 'email', 'phone_number')

@admin.register(User_Address)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'city', 'state', 'country')
    search_fields = ('id','user__username', 'city', 'state', 'country')
