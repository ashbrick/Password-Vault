from django.contrib import admin

# Register your models here.
# customize admin area by bringing in the Password model (will allow you to CRUD passwords)

from .models import Password

admin.site.register(Password)
