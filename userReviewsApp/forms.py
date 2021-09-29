from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project


class SignUpForm(UserCreationForm):
    error_messages = {
    'password_mismatch': ("The two password fields didn't match."),
    }
    email = forms.EmailField(max_length=254, help_text='Required. enter a valid email address.', required=True)
    password1 = forms.CharField(label='Enter password', help_text='your password should be more than 8 characters',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', 
                                widget=forms.PasswordInput)
    username = forms.CharField(help_text="Enter your user name", required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
class ProjectsForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Project
        fields = ('title', 'description', 'link', 'project_image')

        widgets={
            'link': forms.FileInput(attrs={'class':'form-control', 'label':'Project Link'}),
            'title': forms.TextInput(attrs={'class':'form-control', 'label':'Project Title'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'label':'Project description'}),
            'location': forms.Select(attrs={'class':'form-control', 'label':'Project Link'}),
            'project_image': forms.Select(attrs={'class':'form-control', 'label':'Project Home Page Photo'}),
        }
   
