from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *



################################### Invoices's linkded forms ################################### 
class ProdForm(ModelForm):
    """
    Form of Products CRUDS
    """
    def __init__(self, *args, **kwargs):
        super(ProdForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {'class': 'form-control form-control-square'})

    class Meta:

        model = Article
        exclude = ['owner', 'gainMargin','articleType']


class ServForm(ModelForm):
    """
    Form of Services CRUDS
    """
    def __init__(self, *args, **kwargs):
        super(ServForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {'class': 'form-control form-control-square'})

    class Meta:

        model = Article
        exclude = ['owner', 'gainMargin','buyPrice','articleType']