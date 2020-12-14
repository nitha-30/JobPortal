from django.shortcuts import render,redirect
from employer.forms import RegistrationForm,LoginForm,JobpostForm
from django.contrib.auth import authenticate,login,logout
from employer.models import JobPost
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    form=RegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
    return render(request,"employer/registration.html",context)

def signin(request):

    if request.method=="POST":

        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return render(request,"employer/userhome.html")
        else:
            return render(request,"employer/usersignin.html")
    return render(request,"employer/usersignin.html")

def signout(request):
    logout(request)
    return redirect("signin")

@login_required()
def userHome(request):
    return render(request,"employer/userhome.html")

@login_required()
def job_post(request):
    form=JobpostForm(initial={"user":request.user})
    context={}
    context["form"]=form
    if request.method=="POST":
        form=JobpostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listjob")
        else:
            context["form"]=form
            return render(request, "employer/postjob.html", context)
    return render(request,"employer/postjob.html",context)

@login_required()
def list_job(request):
    created_jobs=JobPost.objects.filter(user=request.user)
    context={}
    context["my_job"]=created_jobs
    return render(request,"employer/listjob.html",context)

@login_required()
def delete_job(request,id):
    try:
        JobPost.objects.get(id=id).delete()
        return redirect("listjob")
    except Exception as e:
        return redirect("listjob")