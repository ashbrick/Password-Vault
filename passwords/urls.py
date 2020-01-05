from django.urls import path #bringing in path package

#want url or route that's attached to method in view file, and we want a url for our homepage
from . import views #from all import views

urlpatterns = [ #creating a list for accessing each page
    path('', views.index, name='passwords'), # the '' represents /passwords, and it's calling the index method inside the views file -> views.index is the method, and the name allows us to easily access this path

    path('<int:password_id>', views.password, name='password'), #include id parameter in url
    
    path('search', views.search, name='search'), #anything that has password/ should look at this search file because it's linked to the main urls.py
]
