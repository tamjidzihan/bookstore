from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Profiles)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id','username','name','email','phone','address','phone','date_of_birth','picture']
    list_select_related = ['address']
    ordering = ['username']
    autocomplete_fields = ['user']
    list_select_related = ['user']
    search_fields = ['username']
    list_per_page = 50


@admin.register(models.Address)
class AdressAdmin(admin.ModelAdmin):
    list_display = ['user','street','city','country']
    autocomplete_fields = ['user']
