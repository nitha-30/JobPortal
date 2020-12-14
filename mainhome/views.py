from django.shortcuts import render,redirect

# Create your views here.
def main_home(request):
    return render(request,"mainhome/home.html")