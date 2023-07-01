from django.urls import path 

from .import  views

urlpatterns=[ 
    path('recipire',views.about_recipie), 
    path('addrecipie',views.post_recipie)



]