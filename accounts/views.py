from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here by adding methods from routes (urls.py)

#defining register, takes request as parameter
def register(request):
    if request.method == 'POST':

        # get the data from the form
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # conditional to see if passwords match
        if password == password2:
            return
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        return # log user in
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index') #redirects user to index
    #import redirect

def dashboard(request):
    return render(request, 'accounts/dashboard.html')





#### TESTS ########################################

#==========
#   def register(request):
#==========
    #Testing >>> SUCCESSFUL
    ### create conditional to determine if the request is a POST or GET
    ### if it's equal to post
    ### test to see if post request is made ('SUBMITTED' will show up in terminal)
    ### then redirect back to register page

    # if request.method == 'POST':
    #     print('SUBMITTED')
    #     return redirect('register')

    ### else render the form
    ### and return the requested data and the template it's assigned to

    # else:
    #     return render(request, 'accounts/register.html')
