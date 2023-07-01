from django.shortcuts import render,redirect 

from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 
from .forms import LoginForm 

def register_user(request): 
    if request.method == 'POST' : 
      form=UserCreationForm(request.POST) 
      if form.is_valid():
         form.save() 
         messages.add_message(request,messages.SUCCESS,'new account has been created') 
         return redirect('/register') 
      else:
            messages.add_message(request,messages.ERROR,'something went wrong please verify forms fields')
            return render(request,'accounts/register.html',{'form':form})



    context={
        'form':UserCreationForm
    } 
    return render(request,'accounts/register.html',context)  

def login_user(request): 
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=authenticate(request,username=data['username'],password=data['password'])

            if user is not None:
                login(request,user)
                return redirect('/product')
            else:
                messages.add_message(request,messages.ERROR,'please provide correct credentials')
                return render(request,'accounts/login.html',{'form':form}) 

    context={ 
        'form':LoginForm 
    } 
    return render(request,'accounts/login.html',context)   

def logout_user(request): 
    logout(request)
    return redirect('/login') 

# Create your views here.
