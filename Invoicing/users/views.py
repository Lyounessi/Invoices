from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from .models import *
from django.views import View, generic
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required

############################Company CRUDs##############################################
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.forms import UserCreationForm


################################ user's Views #########################################


def home(request):
    """
    A test home users View before log in
    """
    return render(request, 'users/home.html')


@login_required(login_url='/user/logs/login/')
def dashboard(request):
    """
    this view present a dashboard of user after login
    """
    return render(request, 'users/dashboard/index.html')


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = 'clients:home'



################################ Company's Views #########################################

# @method_decorator(login_required, name='dispatch')
class CreateCompany(CreateView):
    """
    Create New Caompany for a specific user
    """
    model = Company
    template_name = 'users/companys/company.html'
    fields = ('name', 'activityDom', 'logo', 'adress', 'countrie',
              'city', 'postCode', 'email', 'taxNum', 'phone', )
    success_url = reverse_lazy('users:home')

    def form_valid(self, form):
        """
        Add a valid form Calling the auth user and 
        give it as value to the owner field
        """

        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        return super(CreateCompany, self).form_valid(form)

# @method_decorator(login_required, name='dispatch')


class CompanyDetailView(DetailView):
    """
    showing details of a company
    """
    model = Company
    template_name = 'users/companys/details.html'
    context_object_name = 'company'

# @method_decorator(login_required, name='dispatch')


class CompanyUpdateView(UpdateView):
    """
    Update the company's Informations
    """
    model = Company
    template_name = 'users/companys/update.html'
    context_object_name = 'company'
    fields = ('name', 'activityDom', 'logo', 'adress', 'countrie',
              'city', 'postCode', 'email', 'taxNum', 'phone', )

    def get_success_url(self):
        return reverse_lazy('users:companyDetail', kwargs={'pk': self.object.id})


# @method_decorator(login_required, name='dispatch')
class CompanyDeleteView(DeleteView):
    """
    Delete a company
    """
    model = Company
    template_name = 'users/companys/delete.html'
    success_url = reverse_lazy('users:home')
