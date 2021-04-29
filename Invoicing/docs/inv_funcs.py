from .models import *
from datetime import date, datetime
from decimal import Decimal



def firstInvoiceNumber():
    today = date.today()
    return"I-{}-{}".format(today.strftime('%y-%m'), 1) 

def creationInv(req):
    """
    This function is made to make autonubers in every new invoice creted when create invoice
    """
    
    lastSv = Invoices.objects.filter(creator=req.user, back_status='In save').last()
    lastPro = Invoices.objects.filter(creator=req.user, back_status='In Process').last()
    numb= ""
    today = date.today()
           
    if lastSv :     
        idate = datetime.strptime(str(lastSv.dateCreation), '%Y-%m-%d')
        idate =  idate.date().strftime('%y-%m')

        if idate == today.strftime('%y-%m') : 
            number = int(lastSv.number) + 1
            numb = "I-{}-{}".format(today.strftime('%y-%m'), number) 
            invoices = Invoices.objects.create(dateCreation=date.today(),
                creator=req.user, number=number, prov_numb=numb, back_status='In Process')
            print(invoices)
        else:
            number = 1
            numb = "I-{}-{}".format(today.strftime('%y-%m'), number) 
            invoices = Invoices.objects.create(dateCreation=date.today(),
                creator=req.user, number=number, prov_numb=numb, back_status='In Process')
            print(invoices)
   
    if lastPro :     
        idate = datetime.strptime(str(lastPro.dateCreation), '%Y-%m-%d')
        idate =  idate.date().strftime('%y-%m')

        if idate == today.strftime('%y-%m') : 
            number = int(lastPro.number) + 1
            numb = "I-{}-{}".format(today.strftime('%y-%m'), number) 
            invoices = Invoices.objects.create(dateCreation=date.today(),
                creator=req.user, number=number, prov_numb=numb, back_status='In Process')
            print(invoices)
        else:
            number = 1
            numb = "I-{}-{}".format(today.strftime('%y-%m'), number) 
            invoices = Invoices.objects.create(dateCreation=date.today(),
                creator=request.user, number=number, prov_numb=numb, back_status='In Process')
            print(invoices)
      
    

    
    return invoices  


def invoiceDuplicator(invoice, req):
    """
    duplicate a selected invoice
    """

    numb= ""
    today = date.today()
    idate = datetime.strptime(str(invoice.dateCreation), '%Y-%m-%d')
    idate =  idate.date().strftime('%y-%m')

    if idate == today.strftime('%y-%m') : 
        number = int(invoice.number) + 1
        numb = "I-{}-{}".format(today.strftime('%y-%m'), number) 
        newInv = Invoices(title=invoice.title, dateCreation=date.today(), creator=req.user, 
                        client=invoice.client, stats=invoice.stats, 
                        back_status= "In Process",number=number, prov_numb=numb)    
        newInv.save()
        pk = newInv.pk

    else:
        number = 1
        numb = "I-{}-{}".format(today.strftime('%y-%m'), number) 
        newInv = Invoices(title=invoice.title, dateCreation=date.today(), creator=req.user, 
                        client=invoice.client, stats=invoice.stats, 
                        back_status= "In Process",number=number, prov_numb=numb)    
        newInv.save()
    
        pk = newInv.pk
    

    return newInv

def invoiceFinalisator(invoice, req):
    '''
    Update the selected invoice back status to finilised
    '''

    #select last finilised invoice
    last_F_Inv = Invoices.objects.filter(creator=req.user, back_status='Finilised').last()
    numb= ""
    today = date.today()
    idate = datetime.strptime(str(invoice.dateCreation), '%Y-%m-%d')
    idate =  idate.date().strftime('%y-%m')
    if last_F_Inv:    
        total = last_F_Inv.total

        if idate == today.strftime('%y-%m') : 
            number = int(last_F_Inv.number) + 1
            numb = "{}-{}".format(today.strftime('%y-%m'), number) 
            Invoices.objects.filter(pk=invoice.pk).update(back_status='Finilised', 
            number=number, fnb=numb, prov_numb=None, still_to_pay= total)
        else:
            number = 1
            numb = "{}-{}".format(today.strftime('%y-%m'), number) 
            Invoices.objects.filter(pk=invoice.pk).update(back_status='Finilised', 
            number=number, fnb=numb, prov_numb=None, still_to_pay= total)
    else:
            number = 1
            numb = "{}-{}".format(today.strftime('%y-%m'), number) 
            Invoices.objects.filter(pk=invoice.pk).update(back_status='Finilised', 
            number=number, fnb=numb, prov_numb=None, still_to_pay= invoice.total)
           
    return invoice








#########################################
############Updates totals++ ############
#########################################

def subTotal(obj, invoice):
    """
    Updating the sub total
    """
    
    sub_total =  invoice.sub_total
    if sub_total:
        return obj.amount + sub_total
    else:
        sub_total = 0
        return obj.amount + sub_total

def taxConversionInvI(obj, amount, tax):
    """
    convert tax from % to value in $
    """ 
    
    result_tax = 0   
    if tax == None:
        tax = 0
    obj.tax_one +=  Decimal(amount) * Decimal(tax/100)
    result_tax = obj.tax_one
    return result_tax


def taxConversionInvII(obj, amount, tax):
    """
    convert tax from % to value in $
    """ 
    
    result_tax = 0   
    if tax == None:
        tax = 0
    obj.tax_two +=  Decimal(amount) * Decimal(tax/100)
    result_tax = obj.tax_two
    return result_tax

def total(obj, sub):
    """
    Creating the invoice total calculating all elements
    """
        
    return sub + obj.tax_one + obj.tax_two

#########################################
############Updates totals-- ############
#########################################

def subTotal_(obj, invoice):
    """
    Updating the sub total
    """
    sub_total =  invoice.sub_total
    return sub_total - Decimal(obj.amount)   

def taxConversionInv_I(obj, amount, tax):
    """
    convert tax from % to value in $
    """ 
  
    result_tax = obj.tax_one
    if tax == None:
        tax = 0
    result_tax -=  Decimal(amount) * Decimal(tax/100)
    return result_tax


def taxConversionInv_II(obj, amount, tax):
    """
    convert tax from % to value in $
    """ 
   
    result_tax = 0   
    if tax == None:
        tax = 0
    obj.tax_two -=  Decimal(amount) * Decimal(tax/100)
    result_tax = obj.tax_two
    return result_tax

def total_(obj, article):
    """
    Creating the invoice total calculating all elements when delete t
    """
    tax_one = Decimal(article.amount)* Decimal(article.tax_one/100)
    tax_two = Decimal(article.amount)* Decimal(article.tax_two/100)

    return obj.total - (Decimal(article.amount) + tax_one + tax_two)
