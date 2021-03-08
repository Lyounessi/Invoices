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
    form_class = InvoiceForm
    initial = {'key': 'value'}
    template_name = 'docs/invoices/cruds/create.html'
    

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        invoices = Invoices.objects.create(dateCreation=date.today(),
            creator = request.user,)
        invoices = Invoices.objects.filter(creator=request.user).order_by('-id')[:1]
        print(invoices[0].creator)
        invoice = Invoices(
            fnb=autoNumInvoice(invoices[0], request), 
            
            back_status ='insave',
            )
        invc = Invoices.objects.filter(creator=request.user).order_by('-id')[:1]
        print(invc)
        #logo = invoices[0]# Get the logo if exist
        context = {
            'form': form,
            #'logo': logo,
            'invoice': invc[0],
        }
        return render(request, self.template_name, context)

    '''def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        context = {
            'form': form,
        }
        print('-------------------Recieved')
        print(form.errors) 
        if form.is_valid():
            
            print('Valid---------------------')
            clt = form.save(commit=False)
            clt.creator = request.user
            clt.back_status ='insave'
            clt.dateCreation = date.today()
            clt.fnb = autoNumInvoice(clt, request)
            clt.save()
            return redirect('docs:addProds', clt.pk)
                
        else:
            print('-------------Not Valid')
            
            
        return render(request, self.template_name, context=context)'''



def selectClient(request, *args, **kwargs):
    """
    This view is for ajax select and show client infos
    """
    if request.method == "POST" and request.is_ajax():
        datastring = request.body.decode("utf-8")
        print(datastring)
        return JsonResponse({'html_form': html_form})

    else:
        clients = Clients.objects.all()
        context = {'clients': clients}
        html_form = render_to_string('docs/invoices/select_client.html',
            context,
            request=request,
        )
        return JsonResponse({'html_form': html_form})





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







class InvoiceAddProds(View):
    """
    Create and show New Invoice lists for a specific user
    """
    form_class = AddProdsForm
    initial = {'key': 'value'}
    template_name = 'docs/invoices/addprods.html'

    def get(self, request, pk, *args, **kwargs):
        
        form = self.form_class(initial=self.initial)
        invoice = Invoices.objects.filter(pk=pk)
        invoice_prods = Article_Inv.objects.filter(invoice=invoice[0].pk)
        context = {
            'form': form,
            'invoice': invoice[0],
            'prods' : invoice_prods,
       
        }
        return render(request, self.template_name, context)

    '''def post(self, request, pk, *args, **kwargs):
        form = self.form_class(request.POST)
        invoice = Invoices.objects.filter(pk=pk)
        invoice_prods = Article_Inv.objects.filter(invoice=invoice[0].pk)
        pk = pk
        context = {
            'form': form,
            'invoice': invoice[0],
            'prods' : invoice_prods,
        }
        
        if form.is_valid():
              
            
            clt = form.save(commit=False)
            if clt.tax_one >= 0 and clt.tax_two >= 0 and clt.qte >= 0 and clt.remise >= 0 :
                clt.invoice = invoice[0]
                clt.price = pricingInInvoice(clt, clt.article.sellPrice)
                clt.save()
                return redirect('docs:addProds', pk)
            else:
                print('EROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOORRRRRRRRRRRR')

          
                
            
        else:
            print('-------------Not Valid')
            
            
        return render(request, self.template_name, context=context)'''
def addPtoInv(request, *args, **kwargs):
    data = dict()
    if request.method == 'POST':
        form1 = ProdForm
        form2 = ServForm
        if form1.is_valid():
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
            data["form_is_valid"] = True
        elif form2.is_valid():
            clt = form.save(commit=False)
            print('-------------------------------->', request.user)
            clt.owner = request.user
            clt.articleType = 'srv'
            clt.save()
            data["form_is_valid"] = True
        else:
            data['form_is_valid'] = False
    else:
        form1 = ProdForm
        form2 = ServForm
    context = {'form1': form1,
    'form2':form2}
    html_form = render_to_string('docs/invoices/new_article.html',
        context,
        request=request,
    )
    return JsonResponse({'html_form': html_form})
    
        


def dupInvoice(request, pk):
    
    """
    This view is for duplicating a selected invoice
    """
    invoice = Invoices.objects.filter(pk=pk)
    invoice = invoice[0]
    newInv = Invoices(title=invoice.title, dateCreation=date.today(), creator=request.user, 
     client=invoice.client, stats=invoice.stats)
    newInv.save()
   
    if invoice.artice.all() != None:
        for i in invoice.artice.all():# select all manytomany article and add to the new invoice
            newInv.artice.add(i)
    else:
        print("AHDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    newInv.back_status = "insave"
    newInv.fnb = invoiceDupAutoincreaseNumb(newInv, request)
    newInv.save()
    
    
    return render(request,'docs/invoices/duplicate.html', locals())

def finaliseInv(request, pk):
    """
    this view is made to change an invoice's statu, 
    from insave to finalised
    """
    invoice = Invoices.objects.get(pk=pk)
    if invoice.creator == request.user :
        invoice.back_stats = 'finished'
        return redirect('docs:detailsInvoice pk')
    else:
        print('SOMETHING is wrong ///////////////////////////////////')
    return render(request, 'docs:detailsInvoice pk')