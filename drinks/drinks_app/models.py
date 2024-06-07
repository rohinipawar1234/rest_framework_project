from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name + " " + self.description
    

class CustomUser(AbstractUser):

    """User Model Class"""

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    
  
