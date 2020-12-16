from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from docs.models import *
from django.views import View
from django.contrib import messages
from docs.forms import *
from django.contrib.auth.decorators import login_required
############################ In logics imports ##############################
import datetime
from docs.funcs import *
############################Clients CRUDs##############################################
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView



############################### INVOICES VIEWS ###############################


class CreateInvoice(View):
    """
    Create and show New Invoice lists for a specific user
    """
    form_class = InvoiceForm
    initial = {'key': 'value'}
    template_name = 'docs/invoices/cruds/create.html'
    

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        context = {
            'form': form,
        }
        print('-------------------Recieved')
        if form.is_valid():
            print('Valid---------------------')
            clt = form.save(commit=False)
            clt.creator = request.user
            clt.number = autoNumInvoice()
            clt.save()
            return render('docs:home')
        else:
            print('-------------Not Valid')
            
        return render(request, self.template_name, context=context)


class InvoiceDetailsView(DetailView):
    """
    showing details of an invoice
    """
    model = Invoices
    template_name = 'docs/invoices/cruds/details.html'
    context_object_name = 'invoice'



# @method_decorator(login_required, name='dispatch')
class InvoiceDeleteView(DeleteView):
    """
    Delete a selected invoice
    """
    model = Invoices
    template_name = 'docs/invoices/cruds/delete.html'
    success_url = reverse_lazy('docs:home')



class InvoiceUpdateView(UpdateView):
    """
    Update the Invoices's Informations
    """
    model = Invoices
    template_name = 'docs/invoices/cruds/update.html'
    context_object_name = 'invoice'
    fields = ('title', 'logo', 'client', 'stats')

    def get_success_url(self):
        return reverse_lazy('docs:detailsInvoice', kwargs={'pk': self.object.id})