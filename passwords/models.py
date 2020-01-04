from django.db import models

#referenced these docs: https://docs.djangoproject.com/en/3.0/topics/db/models/
# Create your models here.
class Password(models.Model): #defining a class and extending the core model
    #define the fields of the model, each one is specified as a class attribute and each attribute maps to a database column
    #the id column is added by default by django
    website = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.website #this is what will show when all of the info isn't being displayed

#now to create the table in sql using this model, go to terminal and type: $python3 manage.py makemigrations

#you should get a message saying that the model was created, and then if you want to see the CREATE TABLE command for sql you can type: $ python3 manage.py sqlmigrate passwords 0001 (passwords 0001 is the file that was created in the passwords app once the table was created)

#the run the following command to actually run the migration and push the info into the database: $ python3 manage.py migrate -- if everything works it should say "ok"
