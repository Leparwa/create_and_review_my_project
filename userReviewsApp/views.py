from django.contrib.auth import forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from requests.models import Response
from .forms import SignUpForm, ProjectsForm
from .services import register_user, get_user_projects, create_use_project
from django.contrib import messages
def home(request):
    projects= get_user_projects(),
    print(projects)
    return render(request, 'home.html')

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = {
                "username": form.cleaned_data['username'],
                "email": form.cleaned_data['email'],
                "password": form.cleaned_data['password1']
                }
            res = register_user(data)
            return redirect(reverse("home"))
        return redirect(reverse("login"))
    form = SignUpForm()
    return render (request=request, template_name="auth/django_registration/registration_form.html", context={"form": SignUpForm})
def login(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = {
                "email": form.cleaned_data['email'],
                "password": form.cleaned_data['password1']
                }
            res = register_user(data)
            return redirect(reverse("home"))
        return redirect(reverse("login"))
    form = SignUpForm()
    return render (request=request, template_name="auth/django_registration/registration_form.html", context={"form": SignUpForm})
# def get_user_projects(request):
#     if request.method == "GET":
#         return render(request, "users/register.html",{"form": CustomUserCreationForm})
#     elif request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#         return redirect(reverse("home"))
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
