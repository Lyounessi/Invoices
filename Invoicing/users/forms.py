from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


################################ user's Views #########################################

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = (  'username', 'email' , 'password1', 'password2')




class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'User', 'id': 'user-name'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Password',
            'id': 'user-password',
            'type' : 'password',
        }
))





################################ Company's Forms #########################################


class CompanyForm(forms.Form):
    """
    In Case of needs, a comapny For to build
    """
    pass