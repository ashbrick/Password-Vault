from django.shortcuts import render
from django.http import HttpResponse #import this response so can use it in the index method

# Create your views here
def index(request): #defining a method as "index" where a request is passed in as a parameter
    return HttpResponse('<h1>Hello World</h1>') #this is what we want to happen, it'll be the template for the homepage --for now just adding some html to test it 
