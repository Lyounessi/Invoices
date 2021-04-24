from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from docs.models import *
from django.views import View
from django.contrib import messages
from docs.forms import *
from django.contrib.auth.decorators import login_required
############################ In logics imports ##############################
from datetime import date
from docs.inv_funcs import *
############################Clients CRUDs##############################################
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
############################OUTSIDES IMPORTS##############################################
from clients.forms import *
from clients.models import *
from stocks.models import *
from stocks.forms import ProdForm, ServForm



############################### INVOICES VIEWS ###############################


class CreateInvoice(View):
    """
    Create and show New Invoice lists for a specific user
    """
    #form_class = InvoiceForm
    initial = {'key': 'value'}
    template_name = 'docs/invoices/cruds/create.html'
    

    def get(self, request, *args, **kwargs):
        invoice = Invoices.objects.filter(creator=request.user).order_by('-id')[:1]
        context = {}
        
        if invoice:            
            if invoice[0].client == None:  
                artInv = Article_Inv.objects.filter(invoice=invoice[0])#Select Invoice's articles
                context = {
            
                #'logo': logo,
                'invoice': invoice[0],
                'artInv': artInv,
                }
            else:               
                creationInv(request)
                #logo = invoices[0]# Get the logo if exist
                context = {
                    #'logo': logo,
                    'invoice': invoice,
                }
        else:          
            invoices = Invoices.objects.create(dateCreation=date.today(),
                creator = request.user)
            invoice = Invoices.objects.filter(creator=request.user).order_by('-id')[:1]#select the last invoice
            
            Invoices.objects.filter(pk=invoice).update(prov_numb=firstInvoiceNumber(),
            back_status ='In Process', number=1)#Update Infos of the selected invoice
            
            invoice = invoices
            #logo = invoices[0]# Get the logo if exist
            context = {
                #'logo': logo,
                'invoice': invoice,
                'pk': invoice.pk,
            }
        return render(request, self.template_name, context)

#############################################################################
########################### Begin AJAXING INVOICE ###########################
#############################################################################

#-----------------------------Articles----------------------------#
def addPfromInv(request,  *args, **kwargs):
    '''
    This view is made to make a direct new article from the 
    invoice template
    '''
    data = dict()
    invoice = Invoices.objects.filter(creator=request.user).order_by('-id')[:1]

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
    data["html_form"] = render_to_string('docs/invoices/ajax/new_article.html',
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
    invoice = Invoices.objects.filter(creator=request.user).order_by('-id')[:1]
    artInv = Article_Inv.objects.filter(invoice=invoice[0])#Select Invoice's articles
    invc = invoice[0]
    if request.method == 'POST':
        form = AddArticlesForm(request.user, request.POST)
        if form.is_valid():
            clt = form.save(commit=False)
            articlePrice = Article.objects.filter(pk=clt.article.pk)
            clt.amount = (articlePrice[0].sellPrice * clt.qte)-clt.remise
            clt.invoice = invoice[0]            
            Invoices.objects.filter(creator=request.user).update(
                sub_total= subTotal(clt, invoice[0]),
                tax_one= taxConversionInvI(invc, clt.amount, clt.tax_one),
                tax_two= taxConversionInvII(invc, clt.amount, clt.tax_two),   
            )
                       
            Invoices.objects.filter(creator=request.user).update(
                   total = total(invc, subTotal(clt, invc))         
            )
            form.save()
            invoice = Invoices.objects.filter(creator=request.user).order_by('-id')[:1]

            data['form_is_valid'] = True
            data['html_select_article'] = render_to_string('docs/invoices/ajax/partial-articles-list.html', {
                'artInv': artInv
            })
            data['html_total_dynamic'] = render_to_string('docs/invoices/ajax/partial-total-updates.html', {
                'invoice': invoice[0]
            })
        else:
            data['form_is_valid'] = False
    else:
        form = AddArticlesForm(request.user)

    context = {'form': form,
    'artInv': artInv}
    data['html_form'] = render_to_string('docs/invoices/ajax/artInv.html',
        context,

        request=request
    )
    return JsonResponse(data)

def deleteArtFromInv(request, pk, *args, **kwargs):

    '''
    This view is for deleting a specific article from 
    a specific Invoice
    '''
    article = get_object_or_404(Article_Inv, pk=pk)
    data = dict()
    invoice = Invoices.objects.filter(creator=request.user).order_by('-id')[:1]
    invc = invoice[0]
    if request.method == 'POST':
        Invoices.objects.filter(creator=request.user).update(
                sub_total= subTotal_(article, invc),
                tax_one= taxConversionInv_I(invc, article.amount, article.tax_one),
                tax_two= taxConversionInv_II(invc, article.amount, article.tax_two),   
            )
            
            
        Invoices.objects.filter(creator=request.user).update(
                total = total_(invc, article)         
        )
        article.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        artInv =  Article_Inv.objects.filter(invoice=invoice[0])
        data['html_select_article'] = render_to_string('docs/invoices/ajax/partial-articles-list.html', {
            'artInv': artInv
        })
        data['html_total_dynamic'] = render_to_string('docs/invoices/ajax/partial-total-updates.html', {
                'invoice': invoice[0]
            })
    else:
        context = {'article': article}
        data['html_form'] = render_to_string('docs/invoices/ajax/partial-article-delete.html',
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
    invoice = Invoices.objects.filter(creator=request.user).order_by('-id')[:1]
    if request.method == "POST":
        IdClient = request.POST.get("client")
        if IdClient:
            client = Clients.objects.filter(pk=IdClient)
            Invoices.objects.filter(pk=invoice).update(client= client[0],deadlinePay=client[0].payments_conditions)

            data['form_is_valid'] = True

            data['html_select_client'] = render_to_string('docs/invoices/ajax/client-partial-select.html', {
            'client':client[0],
            })
       
    else:
        clients = Clients.objects.filter(createdBy=request.user, actif=True)
        context = {'clients': clients}
        data['html_form'] = render_to_string('docs/invoices/ajax/select_client.html',
            context,
            request=request,
        )


    return JsonResponse(data)


def addClientInv(request,  *args, **kwargs):
    '''
    This view is made to make a direct new client from the 
    invoice template
    '''
    data = dict()
    print('IM HERE YEAH')

    if request.method == 'POST':
        form = ClientForm(request.POST)
       
        if form.is_valid():
            clt = form.save(commit=False)
            clt.actif = True
            clt.createdBy = request.user
            clt.save()
            data["form_is_valid"] = True
            
        
        
    else:
        

        form = ClientForm()
        
    context = {'form': form,
   }
    data["html_form"] = render_to_string('docs/invoices/ajax/partial-new-client.html',
        context,
        request=request,
    )
    return JsonResponse(data)

#-----------------------------INVOICE's OPEARATIONS----------------------------#

###########################################################################
########################### END AJAXING INVOICE ###########################
###########################################################################

###########################################################################
########################### BEGIN INVOICE'S OPREATIONS#####################
###########################################################################
def saveInvoice(request, pk, *args, **kwargs):
    '''
    This view is for saving a specific Invoice
    '''
   
    data = dict()
    invoice = Invoices.objects.filter(creator=request.user).order_by('-id')[:1]
    invc = invoice[0]
    if request.method == 'POST':
        Invoices.objects.filter(pk=pk).update(back_status='In save')
        data['form_is_valid'] = True  # This is just to play along with the existing code
        
        return redirect('docs:createInvoice')
    else:
        context = {'invc':invc}
        data['html_form'] = render_to_string('docs/invoices/ajax_invoic\'es_options/partial-save-option.html',
            context,
            request=request,
        )
    return JsonResponse(data)


def finaliseInv(request, pk):
    """
    this view is made to change an invoice's statu, 
    to finalised
    """
    data = dict()
    invoice = Invoices.objects.get(pk=pk)
    
    if request.method == 'POST':
        invoiceFinalisator(invoice, request)
        data['form_is_valid'] = True  # This is just to play along with the existing code
        return redirect('docs:createInvoice')
    else:
        context = {'invc':invoice}
        data['html_form'] = render_to_string('docs/invoices/ajax_invoic\'es_options/partial-finalise-option.html',
            context,
            request=request,
        )
    return JsonResponse(data)
    



def dupInvoice(request, pk):
    
    """
    This view is for duplicating a selected invoice
    """
    invoice = Invoices.objects.filter(pk=pk)
    invoice = invoice[0]
    invoiceDuplicator(invoice, request)
    context = {
        "invoice": invoiceDuplicator(invoice, request),
        "pk": pk
    }
    
    return render(request,'docs/invoices/others/duplicate.html', context)




###########################################################################
########################### END INVOICE'S OPREATIONS ######################
###########################################################################

#-_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_-

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

