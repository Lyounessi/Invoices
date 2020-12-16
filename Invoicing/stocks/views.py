from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from .models import *
from django.views import View
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
############################ In logics imports ##############################
import datetime
from .funcs import *
from decimal import Decimal
############################Clients CRUDs##############################################
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView




def home(request):
    
    context={

    }

    return render(request, 'stocks/lists.html', context)


############################### INVOICES VIEWS ###############################


class CreateProd(View):
    """
    Create and show New Product/service lists for a specific user
    """
    
    form_class = ProdForm
    initial = {'key': 'value'}
    template_name = 'stocks/create.html'
    

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
            sell = request.POST.get("sellPrice")
            buy = request.POST.get("buyPrice")
            print(sell, type(sell))
            clt = form.save(commit=False)
            print('-------------------------------->', request.user)
            clt.owner = request.user
            clt.gainMargin = Decimal(sell) - Decimal(buy)
            clt.save()
            return redirect('stocks:home')
        else:
            print('noooooooooooooo')
        return render(request, self.template_name, context=context)


class ProdDetailsView(DetailView):
    """
    showing details of an invoice
    """
    pass
    model = Article
    template_name = 'stocks/details.html'
    context_object_name = 'prod'



# @method_decorator(login_required, name='dispatch')
class InvoiceDeleteView(DeleteView):
    """
    Delete a selected invoice
    """
    pass
    #model = Invoices
    #template_name = 'docs/invoices/cruds/delete.html'
    #success_url = reverse_lazy('docs:home')



class InvoiceUpdateView(UpdateView):
    """
    Update the Invoices's Informations
    """
    pass
    #model = Invoices
    #template_name = 'docs/invoices/cruds/update.html'
    #context_object_name = 'invoice'
    #fields = ('title', 'logo', 'client', 'stats')

    #def get_success_url(self):
    #    return reverse_lazy('docs:detailsInvoice', kwargs={'pk': self.object.id})