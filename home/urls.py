from django.urls import path #bringing in path package

#want url or route that's attached to method in view file, and we want a url for our homepage
from . import views #from all import views

urlpatterns = [ #creating a list
    path('', views.index, name='index'), #views.index is the method, and the name allows us to easily access this path
    path('about',views.about, name='about') #creating the method for the about page
]
