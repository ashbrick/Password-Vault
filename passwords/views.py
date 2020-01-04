from django.shortcuts import render

#this will allow us to fetch passwords based on the model, then insert into template in order to loop through passwords in database
from .models import Password #bring in the Password model

# Create your view methods here based on the urls.py for passwords
def index(request): #main passwords page
    #fetch passwords from database by creating a variable and setting it to the variable name
    passwords = Password.objects.all()

    #create a variable to pass in the passwords as parameter for the return render
    context = {
     'passwords': passwords
    }

    return render(request, 'passwords/passwords.html', context)

def password(request): #individual password page, so it will load this template
    return render(request, 'passwords/password.html')

def search(request): #will load the search password html page from urls.py
    return render(request, 'passwords/search.html')
