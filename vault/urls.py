"""vault URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    # parameter explanations:
    # '': this is whatever the first segment of the url for the home app is going to be (the route), going to leave it blank so it can just be a slash -- linking to urls.py of the home app
    # include: need to bring in "include" because it's part of the django package that allows you to connect to the url file, so add it to line 2 after path

    path('passwords/', include('passwords.urls')), #linking the passwords urls.py to the main urls.py by telling it where to look

    path('accounts/', include('accounts.urls')),

    path('admin/', admin.site.urls),
]
