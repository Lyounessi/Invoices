from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *



################################### Invoices's linkded forms ################################### 
class InvoiceForm(ModelForm):
    """
    Form of Invoices CRUDS
    """
    def __init__(self, *args, **kwargs):
        super(InvoiceForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {'class': 'form-control form-control-square'})

    class Meta:

        model = Invoices
        exclude = ['stats','creator', 'dateCreation', 'number']


################################### Invoices's linkded forms ################################### 

class QuoteForm(ModelForm):
    """
    Form of Invoices CRUDS
    """
    def __init__(self, *args, **kwargs):
        super(QuoteForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {'class': 'form-control form-control-square'})

    class Meta:

        model = Quotes
        exclude = ['creator',  'number', 'stats', 'back_status']




################################### Products's added forms ################################### 
class AddArticlesForm(ModelForm):
    """
    Form of adding products to an invoice
    """
    def __init__(self, *args, **kwargs):
        super(AddArticlesForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {'class': 'form-control border-primary'})
        
    class Meta:

        model = Article_Inv
        exclude = ['invoice','amount']



################################### Clients selection forms ################################### 
class SelectClientForm(forms.Select):
    """
    Form of select clients to an invoice
    """
    pass

class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {'class': 'form-control form-control-square'})

    class Meta:

        model = Clients
        exclude = ['actif','createdBy']