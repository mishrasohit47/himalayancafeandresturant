from django.shortcuts import render,redirect
from  .  models  import Recipie 
from .forms import RecipieForm
from django.contrib import messages 
# Create your views here. 

def about_recipie(request):   
    recipies=Recipie.objects.all()

    context={
        'recipies':recipies
    } 
    return render(request,"recipiecalculator/home.html",context)    

def post_recipie(request): 
    if request.method =='POST':
        form=RecipieForm(request.POST,request.FILES)
        if form.is_valid():
            form.save() 
            messages.add_message(request,messages.SUCCESS,'recipie  added') 
            return redirect('/carecipie/addrecipie') 
        else:
            messages.add_message(request,messages.ERROR,'please verify forms fields ') 
            return render(request,'recipiecalculator/addrecipie.html',{'form':form})
    context={
        'form':RecipieForm
    } 
    return render(request,'recipiecalculator/addrecipie.html',context)  

