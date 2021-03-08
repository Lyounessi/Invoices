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
from docs.inv_funcs import *
############################Clients CRUDs##############################################
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView



############################### INVOICES VIEWS ###############################



class CreateQuote(View):
    """
    Create and show New Quote lists for a specific user
    """
    form_class = QuoteForm
    initial = {'key': 'value'}
    template_name = 'docs/quotes/cruds/create.html'
    

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
            clt = form.save(commit=False)
            clt.number = autoNumQuote()
            clt.creator = request.user
            clt.save()
            print('yeeeeeeees')
            return redirect('docs:home')
        else:
            print('noooooooooooooo')
        return render(request, self.template_name, context=context)


class QuoteDetailsView(DetailView):
    """
    showing details of an invoice
    """
    model = Quotes
    template_name = 'docs/quotes/cruds/details.html'
    context_object_name = 'quote'



# @method_decorator(login_required, name='dispatch')
class QuoteDeleteView(DeleteView):
    """
    Delete a selected invoice
    """
    model = Quotes
    template_name = 'docs/quotes/cruds/delete.html'
    success_url = reverse_lazy('docs:detailsQuote')



class QuoteUpdateView(UpdateView):
    """
    Update the Invoices's Informations
    """
    model = Quotes
    template_name = 'docs/quotes/cruds/update.html'
    context_object_name = 'quote'
    fields = ('title', 'logo', 'client', 'stats')

    def get_success_url(self):
        return reverse_lazy('docs:detailsQuote', kwargs={'pk': self.object.id})