from .models import *
from django import forms
class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["first_name","last_name","email","password"]