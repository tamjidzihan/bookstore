from django.db import models
from django.conf import settings

# Create your models here.


class Profiles(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    username = models.CharField(max_length=200,null=False,blank=False)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200,null=True)
    picture = models.ImageField(upload_to='img',blank=True,null=True)
    date_of_birth = models.DateField(null=True)
    
    def email(self):
        return self.user.email

    def __str__(self):
        return self.username



class Address(models.Model):
    street = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    country = models.CharField(max_length=250,null=True)
    user = models.OneToOneField(Profiles,on_delete=models.CASCADE,primary_key=True)

    def __str__(self) -> str:
        return f'{self.street}, {self.city}, {self.country}'