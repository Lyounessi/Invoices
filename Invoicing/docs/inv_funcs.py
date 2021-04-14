from .models import *
from datetime import date, datetime
from decimal import Decimal




'''
   ###########Invoice Updates..#############
            print('IM UPDATING///////////////////////////////:/')
            Invoices.objects.filter(pk=invoice).update(
                sub_total = invoice.sub_total + clt.article.sellPrice,
                tax_one = invoice.tax_one + taxConversionInv(clt.amount, clt.tax_one),
                tax_two = invoice.tax_two  + taxConversionInv(clt.amount, clt.tax_one),
            )
            Invoices.objects.filter(pk=invoice).update(
                total = invoice.sub_total + invoice.tax_one + invoice.tax_two 
            )
            
            ############END INVC UPDATES#############      
'''
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

    

def pricingInInvoice(obj, prodPrice):
    pass
    """
    When adding product to an invoice Caluculating the price
    
    tax = (obj.tax_one + obj.tax_two)/100
    if tax > 0:
        pr = (Decimal(obj.qte) * Decimal(prodPrice)) * Decimal(tax)
    else : 
        pr = Decimal(obj.qte) * Decimal(prodPrice)
    if obj.remise > 0 :
        return pr - obj.remise
    else:
        return "%.2f" % round(pr, 2)
    """

def taxConversionInv(amount,  tax):
    """
    convert tax from % to value in $
    """  
    return  float(amount) * float(tax/100)
def total(obj):
    if obj.sub_total == None:
        obj.sub_total = 0
    if obj.tax_one == None:
        obj.tax_one = 0
    if obj.tax_two == None:
        obj.tax_two = 0
        
    return sum([obj.sub_total, obj.tax_one, obj.tax_two])

def changeStat(obj):
    """
    This function is for changing an invoice status
    """
    pass