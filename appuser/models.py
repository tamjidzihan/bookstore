from django.db import models
from django.conf import settings
from django.contrib import admin


class Customer(models.Model):
    phone = models.CharField(max_length=200,null=True)
    date_of_birth = models.DateField(null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name
        
    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name
    
    def email(self):
        return self.user.email

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        ordering = ['user__first_name', 'user__last_name']



class Address(models.Model):
    street = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    country = models.CharField(max_length=250,null=True)
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)

    def __str__(self) -> str:
        return f'{self.street}, {self.city}, {self.country}'