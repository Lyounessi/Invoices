from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


################################ user's Views #########################################

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Enter Email',
        }
    ))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Enter First Name',
        }
    ))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Enter Last Name',
        }
    ))

    class Meta:
        model = User
        fields = ( 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *arg, **kwargs):
        super(SignUpForm, self).__init__(*arg, **kwargs)
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'



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