from django.urls import path #bringing in path package

#want url or route that's attached to method in view file, and we want a url for our homepage
from . import views #from all import views

urlpatterns = [ #creating a list for accessing each page
    path('', views.index, name='passwords'), # the '' represents /passwords, and it's calling the index method inside the views file -> views.index is the method, and the name allows us to easily access this path

    path('password_show/<int:password_id>', views.password_show, name='password_show'), #include id parameter in url

    # path('password_edit/<int:password_id>', views.password_edit, name='password_edit'),

    path('password_edit/<str:password_id>', views.passwordEdit, name='password_edit'),

    path('search', views.search, name='search'), #anything that has password/ should look at this search file because it's linked to the main urls.py

    # path('create', views.create, name='create'),
    # removed this path because I'm including the create view on the index/passwords page (the create and show all passwords are in the same route since they're on the same page)

    path('delete/<str:password_id>', views.delete, name='delete'),
]
