from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *




class ClientForm(ModelForm):

    class Meta:
        model = Clients
        exclude = ['createdBy']



