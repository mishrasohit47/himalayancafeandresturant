from django.shortcuts import render,redirect
from .models import Product,Category
from .forms import ProductForm,CategoryForm
from django.contrib import messages 
# Create your views here. 

def sakar(request):
    products=Product.objects.all() 
    context={
        'products':products
    } 
    return render(request,'ourproduct/mainpage.html',context) 

def post_product(request): 
    if request.method =='POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save() 
            messages.add_message(request,messages.SUCCESS,'product added') 
            return redirect('/product/addproduct') 
        else:
            messages.add_message(request,messages.ERROR,'please verify forms fields ') 
            return render(request,'ourproduct/addproduct.html',{'form':form})
    context={
        'form':ProductForm
    } 
    return render(request,'ourproduct/addproduct.html',context)  

def delete_product(request,product_id): 
    product=Product.objects.get(id=product_id) 
    product.delete() 
    messages.add_message(request,messages.SUCCESS,'product deleted') 
    return redirect('/product')

def update_product(request,product_id):
    product=Product.objects.get(id=product_id)
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES,instance=product) 
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'product updated')
            return redirect('/product') 
        else:
            messages.add_message(request,messages.ERROR,'please verify from fields')
            return render(request,'ourproduct/updateproduct.html',{'form':form}) 
    context={ 
    'form':ProductForm(instance=product)

    }
    return render(request,'ourproduct/updateproduct.html',context)   

def post_category(request): 
    if request.method =='POST' : 
       form=CategoryForm(request.POST) 
       if form.is_valid() : 
           form.save()  
           messages.add_message(request,messages.SUCCESS,'category added') 
           return redirect('product/addcategory',{'form':form}) 
       else:
           messages.add_message(request,messages.ERROR,'something went wrong,try again ') 
           return render(request,'ourproduct/addcategory.html',{'form':form})

    context={ 
        'form':CategoryForm
    } 
    return render(request,'ourproduct/addcategory.html',context)  

def show_category(request):
    category=Category.objects.all() 
    context={
        'category': category
    } 
    return render(request,'ourproduct/category.html',context)  

def update_category(request,category_id):  
    category=Category.objects.get(id=category_id) 
    if request.method=='POST': 
        form=CategoryForm(request.POST,instance=category) 
        if form.is_valid(): 
            form.save()
            messages.add_message(request,messages.SUCCESS,'category updated')
            return redirect('/product/category')
        else:
            messages.add_message(request,messages.ERROR,'something went wrong try again')
            return render(request,'ourproduct/updatecategory.html',{'form':form})
    context={
        'form':CategoryForm(instance=category)
    }
    return render(request,'ourproduct/updatecategory.html',context) 

def delete_category(request,category_id):
    category=Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request,messages.SUCCESS,'category deleted')
    return redirect('/product/category')


    


