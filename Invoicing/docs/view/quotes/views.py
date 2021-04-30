from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from docs.models import Quotes, Article_Quotes
from django.views import View
from django.contrib import messages
from docs.forms import *
from django.contrib.auth.decorators import login_required
############################ In logics imports ##############################
from datetime import date
from docs.quotes_funcs import *
############################Clients CRUDs##############################################
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
############################OUTSIDES IMPORTS##############################################
from clients.forms import *
from clients.models import *
from stocks.models import *
from stocks.forms import ProdForm, ServForm



############################### Quotes's VIEWS ###############################
class CreateQuote(View):
    """
    Create and show New Invoice lists for a specific user
    """
    #form_class = InvoiceForm
    initial = {'key': 'value'}
    template_name = 'docs/quotes/cruds/create.html'
    

    def get(self, request, *args, **kwargs):
        quote = Quotes.objects.filter(creator=request.user).order_by('-id')[:1]
        context = {}
        if quote:            
            if quote[0].client == None:  
                print(quote[0].pk)
                artQt = Article_Quotes.objects.filter(quote=quote[0])
                context = {
                #'logo': logo,
                'quote': quote[0],
                'artQt': artQt,
                }
            else:               
                creationQuote(request)
                #logo = quotes[0]# Get the logo if exist
                context = {
                    #'logo': logo,
                    'quote': quote[0],
                }
        else:          
            quotes = Quotes.objects.create(dateCreation=date.today(),
                creator = request.user)
            quote = Quotes.objects.filter(creator=request.user).order_by('-id')[:1]#select the last invoice
            
            Quotes.objects.filter(pk=quote).update(prov_numb=firstQuoteNumber(),
            back_status ='In Process', number=1)#Update Infos of the selected invoice
            
            quote = quotes
            
            context = {
                #'logo': logo,
                'quote': quote[0],
                'pk': quote.pk,
            }
        return render(request, self.template_name, context)

#############################################################################
########################### Begin AJAXING Quote ###########################
#############################################################################

#-----------------------------Articles----------------------------#
def addPfromQuote(request,  *args, **kwargs):
    '''
    This view is made to make a direct new article from the 
    invoice template
    '''
    data = dict()
    invoquote = Quotes.objects.filter(creator=request.user).order_by('-id')[:1]

    if request.method == 'POST':
        form1 = ProdForm(request.POST)
        form2 = ServForm(request.POST)
        if form1.is_valid():
            sell = request.POST.get("sellPrice")
            buy = request.POST.get("buyPrice")
            if buy == None:
                buy = 0
            elif sell == None:
                sell = 0
            clt = form1.save(commit=False)           
            clt.owner = request.user
            clt.gainMargin = Decimal(sell) - Decimal(buy)
            clt.articleType = 'prod'          
            clt.save()
            data["form_is_valid"] = True          
        elif form2.is_valid():
            clt = form2.save(commit=False)              
            clt.owner = request.user
            clt.articleType = 'srv'
            clt.save()   
            data["form_is_valid"] = True
        else:
            data['form_is_valid'] = False
    else:
        form1 = ProdForm()
        form2 = ServForm()
    context = {'form1': form1,
    'form2':form2}
    data["html_form"] = render_to_string('docs/quotes/ajax/new_article.html',
        context,
        request=request,
    )
    return JsonResponse(data)

def selecProd(request,  *args, **kwargs):
    '''
    This view is made to add a direct article to the 
    invoice and refresh the template
    '''
    data = dict()
    quote = Quotes.objects.filter(creator=request.user).order_by('-id')[:1]
    artQt = Article_Quotes.objects.filter(quote=quote[0])#Select Invoice's articles
    qt = quote[0]
    if request.method == 'POST':
        form = AddArticlesQuoteForm(request.user, request.POST)
        if form.is_valid():
            clt = form.save(commit=False)
            articlePrice = Article.objects.filter(pk=clt.article.pk)
            clt.amount = (articlePrice[0].sellPrice * clt.qte)-clt.remise
            clt.quote = quote[0]            
            Quotes.objects.filter(creator=request.user).update(
                sub_total= subTotal(clt, quote[0]),
                tax_one= taxConversionInvI(qt, clt.amount, clt.tax_one),
                tax_two= taxConversionInvII(qt, clt.amount, clt.tax_two),   
            )
                       
            Quotes.objects.filter(creator=request.user).update(
                   total = total(qt, subTotal(clt, qt))         
            )
            form.save()
            invoice = Quotes.objects.filter(creator=request.user).order_by('-id')[:1]

            data['form_is_valid'] = True
            data['html_select_article'] = render_to_string('docs/quotes/ajax/partial-articles-list.html', {
                'artQt': artQt
            })
            data['html_total_dynamic'] = render_to_string('docs/quotes/ajax/partial-total-updates.html', {
                'quote': quote[0]
            })
        else:
            data['form_is_valid'] = False
    else:
        form = AddArticlesQuoteForm(request.user)

    context = {'form': form,
    'artQt': artQt}
    data['html_form'] = render_to_string('docs/quotes/ajax/artQt.html',
        context,

        request=request
    )
    return JsonResponse(data)

def deleteArtFromQuote(request, pk, *args, **kwargs):

    '''
    This view is for deleting a specific article from 
    a specific Invoice
    '''
    article = get_object_or_404(Article_Quotes, pk=pk)
    data = dict()
    quote = Quotes.objects.filter(creator=request.user).order_by('-id')[:1]
    qt = quote[0]
    if request.method == 'POST':
        Quotes.objects.filter(creator=request.user).update(
                sub_total= subTotal_(article, qt),
                tax_one= taxConversionInv_I(qt, article.amount, article.tax_one),
                tax_two= taxConversionInv_II(qt, article.amount, article.tax_two),   
            )
            
            
        Quotes.objects.filter(creator=request.user).update(
                total = total_(qt, article)         
        )
        article.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        artQt =  Article_Quotes.objects.filter(quote=quote[0])
        data['html_select_article'] = render_to_string('docs/quotes/ajax/partial-articles-list.html', {
            'artQt': artQt
        })
        data['html_total_dynamic'] = render_to_string('docs/quotes/ajax/partial-total-updates.html', {
                'quote': quote[0]
            })
    else:
        context = {'article': article}
        data['html_form'] = render_to_string('docs/quotes/ajax/partial-article-delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

#-----------------------------Clients----------------------------#
def selectClient(request, *args, **kwargs):
    """
    This view is for ajax select and show client infos
    """
    data = dict()
    quote = Quotes.objects.filter(creator=request.user).order_by('-id')[:1]
    if request.method == "POST":
        IdClient = request.POST.get("client")
        if IdClient:
            client = Clients.objects.filter(pk=IdClient)
            Quotes.objects.filter(pk=quote).update(client= client[0])

            data['form_is_valid'] = True

            data['html_select_client'] = render_to_string('docs/quotes/ajax/client-partial-select.html', {
            'client':client[0],
            })
        return redirect('docs:createQuote')
        
       
    else:
        clients = Clients.objects.filter(createdBy=request.user, actif=True)
        context = {'clients': clients}
        data['html_form'] = render_to_string('docs/quotes/ajax/select_client.html',
            context,
            request=request,
        )


    return JsonResponse(data)


def addClientQuote(request,  *args, **kwargs):
    '''
    This view is made to make a direct new client from the 
    invoice template
    '''
    data = dict()

    if request.method == 'POST':
        form = ClientForm(request.POST)
       
        if form.is_valid():
            clt = form.save(commit=False)
            clt.actif = True
            clt.createdBy = request.user
            clt.save()
            data["form_is_valid"] = True
        return redirect('docs:createQuote')

    else:

        form = ClientForm()
        
    context = {'form': form,
   }
    data["html_form"] = render_to_string('docs/quotes/ajax/partial-new-client.html',
        context,
        request=request,
    )
    return JsonResponse(data)

#-----------------------------Quote's OPEARATIONS----------------------------#

###########################################################################
########################### END AJAXING Quote ###########################
###########################################################################

###########################################################################
########################### BEGIN Quote'S OPREATIONS#####################
###########################################################################
def saveQuote(request, pk, *args, **kwargs):
    '''
    This view is for saving a specific Quote
    '''
   
    data = dict()
    quote = Quotes.objects.filter(creator=request.user).order_by('-id')[:1]
    qt = quote[0]
    if request.method == 'POST':
        Quotes.objects.filter(pk=pk).update(back_status='In save')
        data['form_is_valid'] = True  # This is just to play along with the existing code
        
        return redirect('docs:createQuote')
    else:
        context = {'qt':qt}
        data['html_form'] = render_to_string('docs/quotes/ajax_quote\'s_options/partial-save-option.html',
            context,
            request=request,
        )
    return JsonResponse(data)


def finaliseQuote(request, pk):
    """
    this view is made to change an invoice's statu, 
    to finalised
    """
    data = dict()
    quote = Quotes.objects.get(pk=pk)
    
    if request.method == 'POST':
        quoteFinalisator(quote, request)
        data['form_is_valid'] = True  # This is just to play along with the existing code
        return redirect('docs:createQuote')
    else:
        context = {'qt':quote}
        data['html_form'] = render_to_string('docs/quotes/ajax_quote\'s_options/partial-finalise-option.html',
            context,
            request=request,
        )
    return JsonResponse(data)
    



def dupQuote(request, pk):
    
    """
    This view is for duplicating a selected invoice
    """
    quote = Quotes.objects.filter(pk=pk)
    quote = quote[0]
    quoteDuplicator(quote, request)
    context = {
        "quote": quoteDuplicator(quote, request),
        "pk": pk,
    }
    
    return render(request,'docs/quotes/others/duplicate.html', context)




###########################################################################
########################### END Quote'S OPREATIONS ######################
###########################################################################

#-_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_-

class QuoteDetailsView(DetailView):
    """
    showing details of an invoice
    """
    model = Quotes
    template_name = 'docs/quotes/cruds/details.html'
    context_object_name = 'quote'

    
    

