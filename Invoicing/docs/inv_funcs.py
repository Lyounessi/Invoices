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
