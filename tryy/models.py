from django.db import models
from django.db.models import Model

# Create your models here.
class Product(models.Model):
    id=models.IntegerField(primary_key=True)
    productname = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    
    def __str__(self):
        return self.productname
    
class Signup(models.Model):
    email=models.CharField(max_length=100)
    passsword=models.CharField(max_length=20)
    username=models.CharField(max_length=20,null=True)

# class ok(models.Model):
#     hi=models.CharField(max_length=50)
#     hello=models.CharField(max_length=122)
    
# class ketul(models.Model):
#     name=models.CharField(max_length=100)