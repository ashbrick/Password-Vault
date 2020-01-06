from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here by adding methods from routes (urls.py)

#==================
#   Register
#==================
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
            # check to see if username exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username unavailable')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This email is already registered')
                    return redirect('register')
                else:
                    # if everything matches
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # login automatically after registering
                    auth.login(request, user) #bring in from django.contrib
                    messages.success(request, 'You are registered, and logged in')
                    return redirect('index')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')
#==================
#   LOGIN
#==================
def login(request):
    #check to make sure it's post request (submitting a form)
    if request.method == 'POST':
        #get the variables we need to login
        username = request.POST['username'] # get username from the form
        password = request.POST['password'] # get password from the form

        # create variable called user and set it to auth, then attach the authenticate method and pass 2 parameters: the username and password that were submitted in the form
        # auth was imported above from django.contrib
        user = auth.authenticate(username=username, password=password)

        # see if user can be found in the database
        if user is not None:
            auth.login(request, user) # authorize login based on request and user
            messages.success(request, 'You are logged in') # alert with this message if successful
            return redirect('dashboard') # take user to their dashboard
        else:
            messages.error(request, 'Invalid credentials') # send this message if username or password don't match what's in database
            return redirect('login') # take user back to login page again
    else:
        return render(request, 'accounts/login.html')

#==================
#   LOGOUT
#==================
def logout(request):
    # if it's a post request
    if request.method == 'POST':
        auth.logout(request) # user logout
        messages.success(request, 'You have successfully logged out') #send user message
        return redirect('index') # take them to the index page
    return redirect('index') # redirects user to index
    #import redirect

#==================
#   DASHBOARD
#==================
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
