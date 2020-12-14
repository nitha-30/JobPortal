from django.shortcuts import render, redirect
from candidate.forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from employer.models import JobPost
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def signup(request):
    form = RegistrationForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    return render(request,"candidate/registration.html",context)


def log_in(request):
    if request.method=="POST":

        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return render(request,"candidate/home.html")
        else:
            return render(request,"candidate/candidatesignin.html")
    return render(request,"candidate/candidatesignin.html")
def log_out(request):
    logout(request)
    return redirect("login")
@login_required()
def home(request):
    return render(request,"candidate/home.html")

@login_required()
def all_jobs(request):
    alljobs=JobPost.objects.all()
    context={}
    context["alljobs"]=alljobs
    return render(request,"candidate/alljobs.html",context)

@login_required()
def job_view(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(skills__icontains=query)|Q(experience__icontains=query)|Q(location__icontains=query)

            results= JobPost.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'candidate/viewjobs.html', context)

        else:
            return render(request, 'candidate/viewjobs.html')

    else:
        return render(request, 'candidate/viewjobs.html')


