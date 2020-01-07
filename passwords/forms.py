from django.forms import ModelForm
from .models import Password

# create a class for the form and add name of the model
class PasswordForm(ModelForm): #inherit information from ModelForm
    class Meta:
        model = Password # which model building a form for
        fields = "__all__" # add fields for form, bring in all of the fields

# def __init__(self, user, *args, **kwargs):
#     self.user = user
#     super(PasswordForm, self).__init__(*args, **kwargs)
