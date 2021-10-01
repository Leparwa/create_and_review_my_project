from django.contrib import messages
from django.contrib.auth import forms
from django.contrib.messages.api import error
from django.forms import fields
from django.forms.models import fields_for_model
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from requests.models import Response
from .forms import SignUpForm, ProjectsForm, LoginForm
from .services import register_user, get_user_projects, create_use_project, login_user
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import BadRequest, ValidationError
def home(request):
    projects= get_user_projects()
    return render(request, 'home.html', {'projects': list(projects) })


def register(request):
    if request.method == "POST":
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            data = {
                "username": form.cleaned_data['username'],
                "email": form.cleaned_data['email'],
                "password": form.cleaned_data['password1']
                }
            try:
                print(data)
                res = register_user(data)
                print(res)
            except BadRequest as er:
                return HttpResponse(messages.error(request, message='bad request',))
            messages.success(request, "registered successfully")
            return redirect('home')
    else:
        form = SignUpForm()
    context ={"form":form} 
    return render(request, "django_registration/registration_form.html", context)

                      

    
    
def login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        email = form.data.get('email')
        password = form.data.get('password')
        data ={
            'email':email,
            'password':password
        }
        res = login_user(data)
        if res['Error']:
            return render(request=request,template_name="registration/login.html", context={"errors": res['Error'], "form": LoginForm})
        return redirect(reverse("home"))
    return render (request=request, template_name="registration/login.html", context={"form": LoginForm})
# def get_user_projects(request):
#     if request.method == "GET":
#         return render(request, "users/register.html",{"form": CustomUserCreationForm})
#     elif request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#         return redirect(reverse("home"))
@login_required(login_url='/main/login/')
def create_project(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data = form.instance
            print(data.image.url)
            create_use_project(data)
            return redirect('home')
    else:
        form = ProjectsForm()
    return render(request, 'user_projects/create_project.html', {'form': form})
