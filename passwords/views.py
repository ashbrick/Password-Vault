from django.shortcuts import render

# Create your view methods here based on the urls.py for passwords
def index(request): #main passwords page
    return render(request, 'passwords/passwords.html')

def password(request): #individual password page, so it will load this template
    return render(request, 'passwords/password.html')

def search(request): #will load the search password html page from urls.py
    return render(request, 'passwords/search.html')
