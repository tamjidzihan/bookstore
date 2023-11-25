from django.db import models
from django.conf import settings
from uuid import uuid4

# Create your models here.

class Profile(models.Model):
    # user_id = models.UUIDField(primary_key=True, default=uuid4) // if need add this to the code in future for extra security
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    phone = models.CharField(max_length=200,null=True)
    picture = models.ImageField(upload_to='img',blank=True,null=True)
    date_of_birth = models.DateField(null=True)
    
    def email(self):
        return self.user.email
    
    def first_name(self):
        return self.user.first_name
        
    def last_name(self):
        return self.user.last_name

    def username(self):
        return self.user.username

    def __str__(self):
        return self.user.username


class Addres(models.Model):
    street = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=250)
    country = models.CharField(max_length=250,null=True)
    user = models.OneToOneField(Profile,on_delete=models.CASCADE,primary_key=True,related_name='address')

    def __str__(self) -> str:
        return f'{self.street}, {self.city}, {self.country}'