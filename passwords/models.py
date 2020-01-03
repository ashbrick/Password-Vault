from django.db import models


```referenced these docs: https://docs.djangoproject.com/en/3.0/topics/db/models/```

# Create your models here.
class Password(models.Model): #defining a class and extending the core model
    #define the fields of the model, each one is specified as a class attribute and each attribute maps to a database column
    #the id column is added by default by django
    website = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
