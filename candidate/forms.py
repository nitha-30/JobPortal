from django.contrib.auth.forms import UserCreationForm,User
from django import forms

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField(max_length=120)
    password=forms.CharField(max_length=120)
    def clean(self):
        cleaned_data = super().clean()
        username= cleaned_data.get("username")
        password = cleaned_data.get("password1")
