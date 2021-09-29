import requests
from .serializer import ProjectSerializer
from userReviewsApp import serializer
api_base_url='https://prorater-api.herokuapp.com/'

def register_user(data):
    response=requests.post('http://127.0.0.1:4000/user/register',json=data) 
    print(response.json)
    return response
def login_user(data):
    response=requests.post('http://127.0.0.1:4000/user/login',json=data) 
    print(response.json)
    return response
def get_user(data):
    response=requests.get('http://127.0.0.1:4000/user') 
    print(response.json)
    return response
def get_user_profile(data):
    response=requests.get('http://127.0.0.1:4000/user/profile',json=data) 
    print(response.json)
def create_use_project(data):
    response=requests.post('http://127.0.0.1:4000/project',json=data) 
    print(response.json)
    return response
def get_user_projects():
    response=requests.get('http://127.0.0.1:4000/project')
    res_data =response.json()
    user_data = res_data.get('results')
    return user_data
def get_all_projects():
    response=requests.get('http://127.0.0.1:4000/user/projects') 
    data =response.json()
    return data
   