import json
from django.contrib import messages
from django.contrib.messages.api import error
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import SignUpForm, ProjectsForm, LoginForm
from .services import register_user, get_user_projects, create_use_project, login_user
from django.core.exceptions import BadRequest, ValidationError
@login_required(login_url='/main/login/')
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
                messages.error(request, er)
                return redirect('register')
            messages.success(request, "registered successfully")
            return redirect('home')
    else:
        form = SignUpForm()
    context ={"form":form} 
    return render(request, "django_registration/registration_form.html", context) 
def login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            data = {
                'email':form.cleaned_data.get('email'),
                'password':form.cleaned_data.get('password')
            }
            res = login_user(data)
            if 'Error' in res:
                messages.error(request, res['Error'])
                return redirect(reverse('login'))
            else:
                return redirect('home')
    else:
        form = LoginForm()
    context ={"form":form}
    return render (request, "registration/login.html", context)

def create_project(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.instance
            print(json.dumps(image.project_image.url))
            data ={
                'project_image':json.dumps(image.project_image.url),
                'title':form.cleaned_data.get('title'),
                'description':form.cleaned_data.get('description'),
                'link':form.cleaned_data.get('link')
            }
            re = create_use_project(data)
            print(re)
    else:
        form = ProjectsForm()
    return render(request, 'user_projects/create_project.html', {'form': form})
