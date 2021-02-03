from django.db import models


# Create your models here.
class Authln(models.Model):
    number = models.TextField(max_length=100)
    def __str__(self):
        return self.number

class Custumer(models.Model):
    name = models.CharField(max_length=50) 
    address = models.TextField()
    phone = models.CharField(max_length=50)  
    email = models.EmailField(max_length=254) 
    password = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50) 
    def __str__(self):
        return self.name

   
