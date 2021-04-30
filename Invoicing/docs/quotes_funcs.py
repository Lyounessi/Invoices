from .models import Quotes, Article_Quotes
from datetime import date, datetime
from decimal import Decimal



def firstQuoteNumber():
    today = date.today()
    return"Q-{}-{}".format(today.strftime('%y-%m'), 1) 

def creationQuote(req):
    """
    This function is made to make autonubers in every new quote creted when create quote
    """
    
    lastSv = Quotes.objects.filter(creator=req.user, back_status='In save').last()
    lastPro = Quotes.objects.filter(creator=req.user, back_status='In Process').last()
    numb= ""
    today = date.today()
           
    if lastSv :     
        idate = datetime.strptime(str(lastSv.dateCreation), '%Y-%m-%d')
        idate =  idate.date().strftime('%y-%m')

        if idate == today.strftime('%y-%m') : 
            number = int(lastSv.number) + 1
            numb = "Q-{}-{}".format(today.strftime('%y-%m'), number) 
            quotes = Quotes.objects.create(dateCreation=date.today(),
                creator=req.user, number=number, prov_numb=numb, back_status='In Process')
            
        else:
            number = 1
            numb = "Q-{}-{}".format(today.strftime('%y-%m'), number) 
            quotes = Quotes.objects.create(dateCreation=date.today(),
                creator=req.user, number=number, prov_numb=numb, back_status='In Process')
            
   
    if lastPro :     
        idate = datetime.strptime(str(lastPro.dateCreation), '%Y-%m-%d')
        idate =  idate.date().strftime('%y-%m')

        if idate == today.strftime('%y-%m') : 
            number = int(lastPro.number) + 1
            numb = "Q-{}-{}".format(today.strftime('%y-%m'), number) 
            quotes = Quotes.objects.create(dateCreation=date.today(),
                creator=req.user, number=number, prov_numb=numb, back_status='In Process')
            
        else:
            number = 1
            numb = "Q-{}-{}".format(today.strftime('%y-%m'), number) 
            quotes = Quotes.objects.create(dateCreation=date.today(),
                creator=request.user, number=number, prov_numb=numb, back_status='In Process')
            
      
    

    
    return quotes  


def quoteDuplicator(quote, req):
    """
    duplicate a selected quote
    """

    numb= ""
    today = date.today()
    idate = datetime.strptime(str(quote.dateCreation), '%Y-%m-%d')
    idate =  idate.date().strftime('%y-%m')

    if idate == today.strftime('%y-%m') : 
        number = int(quote.number) + 1
        numb = "I-{}-{}".format(today.strftime('%y-%m'), number) 
        newQt = Quotes(title=quote.title, dateCreation=date.today(), creator=req.user, 
                        client=quote.client, stats=quote.stats, 
                        back_status= "In Process",number=number, prov_numb=numb)    
        newQt.save()
        pk = newQt.pk

    else:
        number = 1
        numb = "I-{}-{}".format(today.strftime('%y-%m'), number) 
        newQt = Quotes(title=quote.title, dateCreation=date.today(), creator=req.user, 
                        client=quote.client, stats=quote.stats, 
                        back_status= "In Process",number=number, prov_numb=numb)    
        newQt.save()
    
        pk = newQt.pk
    

    return newQt

def quoteFinalisator(quote, req):
    '''
    Update the selected invoice back status to finilised
    '''

    #select last finilised invoice
    last_F_quote = Quotes.objects.filter(creator=req.user, back_status='Finilised').last()
    numb= ""
    today = date.today()
    idate = datetime.strptime(str(quote.dateCreation), '%Y-%m-%d')
    idate =  idate.date().strftime('%y-%m')
    if last_F_quote:    
        total = last_F_quote.total

        if idate == today.strftime('%y-%m') : 
            number = int(last_F_quote.number) + 1
            numb = "{}-{}".format(today.strftime('%y-%m'), number) 
            Quotes.objects.filter(pk=quote.pk).update(back_status='Finilised', 
            number=number, fnb=numb, prov_numb=None)
        else:
            number = 1
            numb = "{}-{}".format(today.strftime('%y-%m'), number) 
            Quotes.objects.filter(pk=quote.pk).update(back_status='Finilised', 
            number=number, fnb=numb, prov_numb=None)
    else:
            number = 1
            numb = "{}-{}".format(today.strftime('%y-%m'), number) 
            Quotes.objects.filter(pk=quote.pk).update(back_status='Finilised', 
            number=number, fnb=numb, prov_numb=None)
           
    return quote








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








