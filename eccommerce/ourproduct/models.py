from typing import Iterable, Optional
from django.db import models 
import barcode 
from barcode.writer import ImageWriter 
from io import BytesIO 
from django.core.files import File 
from unicodedata import category 

# Create your models here. 

class Category(models.Model): 
    category_name=models.CharField(max_length=100,unique=True) 
    created_at=models.DateTimeField(auto_now_add=True,null=True)


class Product(models.Model):
    product_name=models.CharField(max_length=100) 
    product_price=models.FloatField()
    product_description=models.TextField()
    image=models.FileField(upload_to='static/uploads',null=True)
    prepared_at=models.DateTimeField(auto_now_add=True,null=True) 
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)     
   

    

    def __str__(self):
       return self.product_name      
    

    