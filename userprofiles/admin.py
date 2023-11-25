from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id','username','first_name','last_name','email','address','phone','date_of_birth','picture']
    list_select_related = ['address']
    ordering = ['user_id']
    autocomplete_fields = ['user']
    list_select_related = ['user']
    search_fields = ['username']
    list_per_page = 50


@admin.register(models.Addres)
class AdressAdmin(admin.ModelAdmin):
    list_display = ['user','street','city','country']
    autocomplete_fields = ['user']
