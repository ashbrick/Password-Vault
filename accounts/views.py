from django.shortcuts import render, redirect

# Create your views here by adding methods from routes (urls.py)

#defining register, takes request as parameter
def register(request):
    #conditional to determine if the request is a POST or GET
    if request.method == 'POST': #if it's equal to post
        print('SUBMITTED') #testing to see if post request is made (will show up in terminal)
        return redirect('register') #then redirect back to register page
        
    else: #else render the form
    #return the requested data and the template it's assigned to
        return render(request, 'accounts/register.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index') #redirects user to index
    #import redirect

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
