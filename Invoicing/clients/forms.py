from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *


# class ClientForm(ModelForm):

#     class Meta:
#         model = Clients
#         exclude = ['createdBy']


class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {'class': 'form-control form-control-square'})

    class Meta:

        model = Clients
        exclude = ['createdBy']
