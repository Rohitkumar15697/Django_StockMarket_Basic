from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class signup_form(UserCreationForm):
    
    email=forms.CharField(max_length=100, required=True)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']


class login_form(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100, widget=forms.PasswordInput)