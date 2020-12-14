from django.contrib.auth.forms import User, UserCreationForm
from django import forms
from employer.models import JobPost
from django.forms import ModelForm


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

class JobpostForm(ModelForm):
    class Meta:
        model=JobPost
        fields=["user","company_name","job_role","skills","experience","location"]