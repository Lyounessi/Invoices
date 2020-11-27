from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from docs.models import *
from django.views import View
from django.contrib import messages
from docs.forms import *
from django.contrib.auth.decorators import login_required
############################ In logics imports ##############################
import datetime
############################Clients CRUDs##############################################
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView



############################### INVOICES VIEWS ###############################


class CreateInvoice(View):
    """
    Create and show New Clients lists for a specific user
    """
    form_class = InvoiceForm
    initial = {'key': 'value'}
    template_name = 'docs/invoices/create.html'
    

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
        if form.is_valid():
            print('yeeeeeeees')
            clt = form.save(commit=False)
            print(request.user)
            clt.creator = request.user
            clt.number = str(request.user)
            clt.save()
            return redirect('clients:home')
        else:
            print('noooooooooooooo')
        return render(request, self.template_name, context=context)


class ClientDetailsView(DetailView):
    """
    showing details of a company
    """
    model = Clients
    template_name = 'clients/cruds/details.html'
    context_object_name = 'client'



# @method_decorator(login_required, name='dispatch')
class ClientDeleteView(DeleteView):
    """
    Delete a client
    """
    model = Clients
    template_name = 'clients/cruds/delete.html'
    success_url = reverse_lazy('clients:home')
