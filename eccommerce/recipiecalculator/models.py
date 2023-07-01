from django.db import models 
from django.contrib.auth.models import User

# Create your models here.

class Recipie(models.Model):
    title=models.CharField(max_length=100) 
    description=models.TextField()  
    direction=models.CharField(max_length=250) 
    date_posted=models.DateField(auto_now_add=True,null=True)  
    created_at=models.DateTimeField(auto_now_add=True,null=True) 
    updated_at=models.DateTimeField(auto_now=True)  
    chief=models.ForeignKey(User,on_delete=models.CASCADE,null=True) 

    def __str__(self): 
        return self.title    
    

    


