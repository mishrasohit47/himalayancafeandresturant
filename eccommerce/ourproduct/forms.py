from django.forms import ModelForm,fields 
from .models import Product,Category


class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields='__all__'  
        # fields=['product_name','product_price'] for defining particular field    

class CategoryForm(ModelForm): 
    class Meta: 
        model=Category 
        fields='__all__'


       
        