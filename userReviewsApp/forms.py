from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Project
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.password_validation import validate_password

class LoginForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. enter a valid email address.', required=True)
    password = forms.CharField(label='Enter password', help_text='your password should be more than 8 characters',
                                widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('email', 'password', )

class SignUpForm(UserCreationForm):
    error_messages = {
    'password_mismatch': "The two password fields didn't match.",
    }
    email = forms.EmailField(max_length=254, help_text='Required. enter a valid email address.', required=True)
    password1 = forms.CharField(label='Enter password', help_text='your password should be more than 8 characters',
                                widget=forms.PasswordInput,)
    password2 = forms.CharField(label='Confirm password', 
                                widget=forms.PasswordInput)
    username = forms.CharField(help_text="Enter your user name", required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2
    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                validate_password(password, self.instance)
            except forms.ValidationError as error:
                self.add_error('password2', error)
    
    def save(self):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'username')

    def clean_password(self):
        return self.initial['password']
class ProjectsForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Project
        fields = ('title', 'description', 'link', 'project_image')

        widgets={
            'link': forms.TextInput(attrs={'class':'form-control', 'label':'Project Link'}),
            'title': forms.TextInput(attrs={'class':'form-control', 'label':'Project Title'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'label':'Project description'}),
            'location': forms.TextInput(attrs={'class':'form-control', 'label':'Project Link'}),
            'project_image': forms.FileInput(attrs={'class':'form-control', 'label':'Project Home Page Photo'}),
        }
   
