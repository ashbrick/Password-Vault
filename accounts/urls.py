from django.urls import path #bringing in path package

#want url or route that's attached to method in view file, and we want a url for our homepage
from . import views #from all import views

#setting up routes
urlpatterns = [ #creating a list for accessing each page
    path('login', views.login, name='login'),

    path('register', views.register, name='register'),

    path('logout', views.logout, name='logout'), 
]
