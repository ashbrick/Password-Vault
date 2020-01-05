from django.shortcuts import get_object_or_404, render

#this will allow us to fetch passwords based on the model, then insert into template in order to loop through passwords in database
from .models import Password #bring in the Password model

# Create your view methods here based on the urls.py for passwords

#==================
#   INDEX PAGE: method for the index/home page
#==================
def index(request): #main passwords page
    #fetch passwords from database by creating a variable and setting it to the variable name
    passwords = Password.objects.all() #shows all password info from db


    #create a variable to pass in the passwords as parameter for the return render
    context = {
     'passwords': passwords
    }
    #load this template to show the index of all passwords
    return render(request, 'passwords/passwords.html', context)

#==================
#   SHOW PAGE: method for single password view
#==================
def password(request, password_id): #individual password page, setting the parameters as request (to request page load) and password_id (to pull data based on the password_id) will load this template
    password = get_object_or_404(Password, pk=password_id) #variable that checks to see if the individual listing page exists and if not it will show a 404 not found page, passing in 2 parameters: the model and the primaary key/id. password_id is also being passed in as a parameter in the urls.py file for the single listing path inside the urlpatterns list ( as '<int:password_id>' ) which shows the id of the individual password in the browser
    #have to bring in the "get_object_or_404" method by importing it from django.shortcuts (top of page)

    context = {
    'password': password
    }

    return render(request, 'passwords/password.html', context)
        # password.html is the template for showing one password
        # context parameter is the variable where the schema/model info for an individual password is stored based on the password variable (where get_object... is stored above)

#==================
#   SEARCH/QUERY: method for search form
#==================

#will load the search password html page from urls.py
def search(request):
    queryset_list = Password.objects.order_by('website') #setting it to the Password model, to pull in all of the password objects, and will alphabetize them (order_by)

    # add filter for website
    # test to see if it exists
    if 'website' in request.GET:
        website = request.GET['website'] # if it exists then get the value of website and store in variable website
        if website: # filtering it based on the data chosen by the dropdown
            queryset_list = queryset_list.filter(website__iexact=website)

    context = {
        'passwords': queryset_list
    }

    return render(request, 'passwords/search.html', context)





############### CODE GRAVEYARD #################

# ----- INDEX ORDER_BY ERROR> this ended up not working because i entered the dummy websites starting with www. so it was only recognizing the w's // solution: a search feature instead
#    passwords = Password.objects.all().order_by('website') #should alphebetize based on the first letter of each word, ascending is default, but if you want to go in descending order then use '-website'


# ----- SEARCH ERROR -----> couldn't retrieve data and redirect to show page
# def search(request): #will load the search password html page from urls.py
#     password = get_object(Password, k=password_website)
#     context = {
#     'password': password
#     }
#     return render(request, 'passwords/search.html')
