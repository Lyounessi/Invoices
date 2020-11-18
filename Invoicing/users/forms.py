from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


################################ user's Views #########################################

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = (  'username', 'email' , 'password1', 'password2')

















################################ Company's Forms #########################################


class CompanyForm(forms.Form):
    """
    In Case of needs, a comapny For to build
    """
    pass