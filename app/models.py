import email
from statistics import mode
from unicodedata import name
from django.db import models

# Create your models here.
class login_data(models.Model):
    name=models.CharField(max_length=30,null=False)
    email=models.EmailField(max_length=30,null=False)
    password=models.CharField(max_length=20,null=False)
    
    def __str__(self):
        return self.name