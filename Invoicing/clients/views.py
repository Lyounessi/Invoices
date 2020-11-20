from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from .models import *
from django.views import View
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
############################Clients CRUDs##############################################
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView




def home(request):
    return render(request, 'clients/home.html')





@method_decorator(login_required, name='dispatch')
class CreateClient(View):
    """
    Create and show New Clients lists for a specific user
    """
    form_class = ClientForm
    clients = Clients.objects.all()
    initial = {'key': 'value'}
    template_name = 'clients/cruds/list.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        context = {
            'form':form,
            'clients':self.clients
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        context = {
            'form':form,
            'clients':self.clients
        }
        if form.is_valid():
            clt = form.save(commit=False)
            clt.createdBy = request.user
            clt.save()
            return redirect('clients:home')
        return render(request, self.template_name, context)


