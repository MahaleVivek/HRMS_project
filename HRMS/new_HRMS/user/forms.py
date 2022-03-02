from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField 
from django.contrib.auth.models import User
#from .models import Profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='First Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name","email", "password1", "password2")

    # def save(self, commit=True):
    #     user = super(SignUpForm, self).save(commit=False)
    #     user.email = self.cleaned_data["email"]
    #     if commit:
    #         user.save()
    #     return user
    
    
