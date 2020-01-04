from django.shortcuts import render
from django.http import HttpResponse #import this response so can use it in the index method

#bring in password model
#from passwords app models, import Password
from passwords.models import Password

# Create your views here

#=================
#   INDEX/HOME ROUTE
#=================
def index(request): #defining a method as "index" where a request is passed in as a parameter
    #return HttpResponse('<h1>Hello World</h1>') #this is what we want to happen, it'll be the template for the homepage --for now just adding some html to test it

    #changed this method to what's below after commenting out the "return HttpResponse"
    return render(request, 'homeapp/index.html') #telling it where to find the template for this page

#=================
#   ABOUT ROUTE
#=================
def about(request):
    return render(request, 'homeapp/about.html')
