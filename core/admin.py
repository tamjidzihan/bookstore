from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from .models import *
# Register your models here.


@admin.register(User)
class UserAdmin(BaseAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide"),
                "fields": ("email","username","first_name","last_name","password1", "password2"),
            },
        ),
    )
