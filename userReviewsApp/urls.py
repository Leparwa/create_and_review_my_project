from django.urls import path, include
from . import views
urlpatterns =[
    path('', views.home, name='home'),
    path("register/", views.register, name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('create-project', views.create_project, name='project'),
] 