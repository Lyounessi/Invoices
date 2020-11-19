from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from .models import *
from django.views import View
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
############################Clients CRUDs##############################################
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView




def home(request):
    return render(request, 'clients/home.html')





@method_decorator(login_required, name='dispatch')
class CreateClient(CreateView):
    """
    Create New Caompany for a specific user
    """
    model = Clients
    template_name = 'clients/cruds/create.html'
    fields = ('companyName', 'name', 'firstName', 'adress', 'countrie', 'city', 'postCode', 'email', 'taxNum', 'phone', 'website' )
    success_url = reverse_lazy('clients:home')
   
   
    def form_valid(self, form):
        """
        Add a valid form Calling the auth user and 
        give it as value to the owner field
        """
        obj = form.save(commit=False)
        obj.createdBy = self.request.user
        obj.save()        
        return super(CreateClient, self).form_valid(form)



