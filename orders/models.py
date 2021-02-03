from django.db import models
from product.models import Products
from authln.models import Custumer
# Create your models here.
class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
         ('on track','on track'),
         ('Delivered','Delivered'),
         
    )
    product = models.ForeignKey(Products,on_delete=models.SET_NULL, null=True )
    delivery_address = models.CharField (max_length=100)
    delivery_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    custumer= models.ForeignKey(Custumer, on_delete=models.SET_NULL, null= True )
    delivery_status = models.CharField(max_length=20, choices=STATUS, default="Pending")
    def __str__(self):
        return self.custumer.name


class ShoppingList(models.Model):
    customer = models.ForeignKey(Custumer,on_delete=models.SET_NULL, null=True, related_name="shoping_customer")
    products = models.ManyToManyField(Products,  blank=True)
    def __str__(self):
        return self.customer.email

# product - category
# ShoppingList has one customer
# Shoping list has many products
# one customer can have many products in shoping list
# list of products of that particular customer 

# ShoppingList one to one Customer 
# ShoppingList many to many Products
 




    


# amarritu - 
# amarRtitu - lower camel case
# AmarRitu - upper caeml case
# amar-ritu - css
# amar_ritu = variables 