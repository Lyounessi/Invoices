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
from datetime import date
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
        invoices = Invoices.objects.filter(creator=request.user).order_by('-id')[:1]
        
        #logo = invoices[0]# Get the logo if exist
        context = {
            'form': form,
            #'logo': logo,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        context = {
            'form': form,
        }
        print('-------------------Recieved')
        print(form.errors) 
        if form.is_valid():
            
            print('Valid---------------------')
            clt = form.save(commit=False)
            clt.creator = request.user
            clt.back_status =statusInv(clt, request)
            clt.dateCreation = date.today()
            clt.fnb = autoNumInvoice(clt, request)
            clt.save()
            return redirect('docs:home')
                
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
    fields = ('stats', 'dateCreation', 'client')
    #print(form.errors)
    def get_success_url(self):
        return reverse_lazy('docs:detailsInvoice', kwargs={'pk': self.object.id})