from django import forms
from .models import Password

class PostForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = "__all__"
