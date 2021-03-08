from .models import *
from datetime import date, datetime
from decimal import Decimal





def autoNumInvoice(obj, req):
    """
    This function is made to make autonubers in every new invoice creted when create invoice
    """
    #lastIn = Invoices.objects.filter(creator=req.user, back_status='finished').last()
    lastSv = Invoices.objects.filter(pk=obj.pk, back_status='insave').last()

    numb=""
    today = date.today()
    
    
    if lastSv:
        idate = datetime.strptime(str(lastSv.dateCreation), '%Y-%m-%d')
        idate =  idate.date().strftime('%y-%m')
        print('////////////////////////////////////////////',lastSv)
        if idate == today.strftime('%y-%m') :
            obj.prov_numb = int(lastSv.prov_numb) + 1 # Increse number
            numb = "I-{}-{}".format(today.strftime('%y-%m'), obj.prov_numb) 
        else:   
            obj.prov_numb = 1
            numb = "I-{}-{}".format(today.strftime('%y-%m'), obj.prov_numb) 
        
    elif not lastSv :
        
        obj.prov_numb = 1
        numb = "I-{}-{}".format(today.strftime('%y-%m'), obj.prov_numb) 
    '''if lastIn and 'fin' in req.POST:
             
       
        idate = datetime.strptime(str(lastIn.dateCreation), '%Y-%m-%d')
        idate =  idate.date().strftime('%y-%m')
        if idate == today.strftime('%y-%m') :
            obj.number = int(lastIn.number) + 1 # Increse number
            numb = "{}-{}".format(today.strftime('%y-%m'), obj.number) 
        else:   
            obj.number = 1
            numb = "{}-{}".format(today.strftime('%y-%m'), obj.number) 
        
    elif not lastIn :
        if 'fin' in req.POST:
            obj.number = 1
            numb = "{}-{}".format(today.strftime('%y-%m'), obj.number)  
    '''        
    return numb  


def invoiceDupAutoincreaseNumb(obj, req):
    """
    create invoice number in duplication view
    """

    lastSv = Invoices.objects.filter(creator=req.user, back_status='insave').last()
    today = date.today()
    if  lastSv:
          
        idate = datetime.strptime(str(lastSv.dateCreation), '%Y-%m-%d')
        idate =  idate.date().strftime('%y-%m')
        
        if idate == today.strftime('%y-%m') :
            obj.prov_numb = int(lastSv.prov_numb) + 1 # Increse number
            numb = "I-{}-{}".format(today.strftime('%y-%m'), obj.prov_numb) 
        else:   
            obj.prov_numb = 1
            numb = "I-{}-{}".format(today.strftime('%y-%m'), obj.prov_numb) 
    
    return numb



def pricingInInvoice(obj, prodPrice):
    """
    When adding product to an invoice Caluculating the price
    """
    tax = (obj.tax_one + obj.tax_two)/100
    pr = (Decimal(obj.qte) * Decimal(prodPrice)) * Decimal(tax)
    if obj.remise > 0 :
        return pr - obj.remise
    else:
        return "%.2f" % round(pr, 2)


def changeStat(obj):
    """
    This function is for changing an invoice status
    """
    pass