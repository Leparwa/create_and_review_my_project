import json
from django.http.response import JsonResponse
import requests
from .serializer import ProjectSerializer
# from userReviewsApp import serializer
from django.core import serializers

api_base_url='https://prorater-api.herokuapp.com/'

def register_user(data):
    response=requests.post('https://api-prorater.herokuapp.com/user/register',json=data) 
    print(response.json)
    return response.json()
def login_user(data):
    response=requests.post('https://api-prorater.herokuapp.com/user/login', json=data) 
    print(response.json())
    return response.json()
def get_user(data):
    response=requests.get('https://api-prorater.herokuapp.com/user') 
    print(response)
    return response
def get_user_profile(data):
    response=requests.get('https://api-prorater.herokuapp.com/user/profile',json=data) 
    print(response.json)
def create_use_project(data):
    print(data)
    response=requests.post('https://api-prorater.herokuapp.com/project/',data) 
    return response
def get_user_projects():
    all_projects=requests.get('https://api-prorater.herokuapp.com/project')
    user_data = all_projects.json()
    return user_data
def get_all_projects():
    response=requests.get('https://api-prorater.herokuapp.com/user/projects') 
    data =response.json()
    return data
   