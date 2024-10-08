from typing import Any
from django.db import models

class Contact(models.Model):
    email=models.CharField(max_length=30)
    feedback=models.TextField()

    def __str__(self):
        return self.email
    
class Home(models.Model):
    img =models.ImageField(upload_to='media')
    name=models.CharField(max_length=20)
    price=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Order(models.Model):
    img =models.ImageField(upload_to='media')
    name=models.CharField(max_length=20)
    price=models.IntegerField(default=0)

    def __str__(self):
        return self.name
 

class Userslogin(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    img =models.ImageField(upload_to='media',default='1.jpeg')
    username=models.CharField(max_length=20,default='m')
    price=models.IntegerField(default=0)
    quantity=models.PositiveIntegerField(default=1)
    item_name=models.CharField(max_length=40,default='a')
    total_price=models.IntegerField(default=0)

    def __str__(self):
        return self.item_name

    