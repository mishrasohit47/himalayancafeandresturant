from django.forms import ModelForm,fields 
from .models import Recipie


class RecipieForm(ModelForm):
    class Meta:
        model=Recipie
        fields='__all__'  
        # fields=['product_name','product_price'] for defining particular field    
