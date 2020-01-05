from django.shortcuts import render, redirect

# Create your views here by adding methods from routes (urls.py)

#defining register, takes request as parameter
def register(request):
    #return the requested data and the template it's assigned to
    return render(request, 'accounts/register.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index') #redirects user to index
    #import redirect

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
