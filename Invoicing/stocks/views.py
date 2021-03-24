import json
from django.http import JsonResponse,  HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from .models import *
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string, get_template

############################ In logics imports ##############################
import datetime
from .funcs import *
from decimal import Decimal
############################Stocks CRUDs##############################################
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView




def home(request):
    articles = Article.objects.filter(owner=request.user, actif=True)
    
    context={
        'articles':articles,
    }

    return render(request, 'stocks/home.html', context)


############################### Stock's VIEWS ###############################


class CreateProd(View):
    """
    Create New Products for a specific user
    """
    
    form_class = ProdForm
    initial = {'key': 'value'}
    template_name = 'stocks/cruds/createProd.html'
    

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        context = {
            'form':form,
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
            if buy == None:
                buy = 0
            elif sell == None:
                sell = 0
            clt = form.save(commit=False)
            print('-------------------------------->', request.user)
            clt.owner = request.user
            clt.gainMargin = Decimal(sell) - Decimal(buy)
            clt.articleType = 'prod'
            clt.save()
            return redirect('stocks:home')
        else:
            print('noooooooooooooo')
        return render(request, self.template_name, context=context)



class CreateServ(View):
    """
    Create  New Services for a specific user
    """
    
    form_class = ServForm
    initial = {'key': 'value'}
    template_name = 'stocks/cruds/createServ.html'
    

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        context = {
            'form':form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        
        form = self.form_class(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            
            clt = form.save(commit=False)
            print('-------------------------------->', request.user)
            clt.owner = request.user
            clt.articleType = 'srv'
            clt.save()
            return redirect('stocks:home')
        else:
            print('noooooooooooooo')
        return render(request, self.template_name, context=context)


class ProdDetailsView(DetailView):
    """
    showing details of an invoice
    """
    model = Article
    template_name = 'stocks/cruds/details.html'
    context_object_name = 'article'

def createUnit(request):
    '''
    This view is for Adding a new units
    '''
    data = dict()

    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            
            data['html_book_list'] = render_to_string('stocks/home.html', {

            })
        else:
            data['form_is_valid'] = False
    else:
        form = UnitForm()

    context = {'form': form}
    data['html_form'] = render_to_string('stocks/ajax/partial-unit-add.html',
        context,
        request=request
    )
    return JsonResponse(data)



def deactivateArticle(request, pk, *args, **kwargs):
    '''
    This view is for Deleting a specific client from 
    the Article's list
    '''
    article = get_object_or_404(Article, pk=pk)
    data = dict()
   
    if request.method == 'POST':
        data['form_is_valid'] = True  # This is just to play along with the existing code
        Article.objects.filter(pk=article.pk).update(actif=False)
        data['article'] = render_to_string('stocks/home.html', {
            'article': article,
        })
    else:
        context = {'article': article}
        data['html_form'] = render_to_string('stocks/ajax/partial-deactivate-article.html',
            context,
            request=request,
        )
    return JsonResponse(data)

def articleUpdateView(request, pk): 
    '''
    update view for articles 
    '''
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
    # fetch the object related to passed id 
    obj = get_object_or_404(Article, pk = pk) 
    print('/////////////////////////////////////',obj.articleType)
    if obj.articleType == 'product' :
        form = ProdForm(request.POST or None, instance = obj) 
    else:
        form = ServForm(request.POST or None, instance = obj) 

    # save the data from the form and 
    # redirect to detail_view 
    if form.is_valid(): 
        #elt = form.save(commit=False)
        
        form.save() 
        return redirect("stocks:home") 
    else:
        
        context["form"] = form 
    # add form dictionary to context 
    context["form"] = form 
  
    return render(request, "stocks/cruds/update.html", context) 
