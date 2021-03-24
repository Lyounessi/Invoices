import json
from django.http import JsonResponse,  HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from .models import *
from django.views import View
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from .funcs import cNumbs
from django.template.loader import render_to_string, get_template
############################Clients CRUDs##############################################
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
############################External imports ##############################################
from docs.models import Invoices


def home(request):
    '''
    List and clients's home page
    '''
    template_name = 'clients/home.html'
    clients = Clients.objects.filter(createdBy=request.user, actif=True)
    context = {
        
        'clients': clients,
    }
    return render(request, template_name, context)

# @method_decorator(login_required, name='dispatch')
class CreateClient(View):
    """
    Create and show New Clients lists for a specific user
    """
    form_class = ClientForm
    initial = {'key': 'value'}
    template_name = 'clients/cruds/create.html'

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
            clt.createdBy = request.user
            clt.number = cNumbs(Clients, request)
            clt.save()
            return redirect('clients:home')
        else:
            print(form.errors)
            messages.error(request, 'something went wrong')
        return render(request, self.template_name, context)


class ClientDetailsView(DetailView):
    """
    showing details of a company
    """
    model = Clients
    template_name = 'clients/cruds/details.html'
    context_object_name = 'client'
    



def deactivateClient(request, pk, *args, **kwargs):

    '''
    This view is for deleting a specific client from 
    the client's list
    '''
    client = get_object_or_404(Clients, pk=pk)
    data = dict()
    if request.method == 'POST':
        data['form_is_valid'] = True  # This is just to play along with the existing code
        Clients.objects.filter(pk=client.pk).update(actif=False)
        data['html_deactivate_client'] = render_to_string('clients/home.html', {
            'client': client
        })
    else:
        context = {'client': client}
        data['html_form'] = render_to_string('clients/ajax/partial-deactivate-client.html',
            context,
            request=request,
        )
    return JsonResponse(data)

def clientUpdateView(request, pk): 
    '''
    update view for articles 
    '''
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
    # fetch the object related to passed id 
    obj = get_object_or_404(Clients, pk = pk)    
    form = ClientForm(request.POST or None, instance = obj) 
    # save the data from the form and 
    # redirect to detail_view 
    if form.is_valid():           
        form.save() 
        return redirect("clients:home") 
    else:
        print('//////////////////////////////', form.errors)

        context["form"] = form 
    # add form dictionary to context 
    context["form"] = form 
    
  
    return render(request, "clients/cruds/update.html", context) 
