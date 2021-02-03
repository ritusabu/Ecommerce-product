from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    name = models.CharField( max_length=50)

    def __str__(self):
        return self.name

from django.utils.html import mark_safe
class Products(models.Model):
    best = models.BooleanField(default=False)
    name = models.CharField( max_length=50)
    price = models.FloatField()
    description = RichTextField()
    image = models.ImageField( upload_to="products_img/")
    rating = models.FloatField()
    discount = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def image_tag(self):
            return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.image.url))

    image_tag.short_description = 'Image'
    

class Review(models.Model):
    messege = models.CharField( max_length=100)
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.messege

# Review and Product -> 
# Review has one and only one product
# Product has many reviews
# Product has one and only one cateogoty
# Catgory has many productts


class Offer(models.Model):
    name = models.TextField(max_length=100)
    products = models.ManyToManyField(Products,  blank=True)
    def __str__(self):
        return self.name +" "+ str(self.id)

# offers has list of products many to many m2m
# offers has only one product5 foregin key