from .models import *
from datetime import date, datetime





def autoNumInvoice(obj, req):
    """
    This function is made to make autonubers in every new invoice creted
    """
    lastIn = Invoices.objects.filter(creator=req.user, back_status='finished').last()
    lastSv = Invoices.objects.filter(creator=req.user, back_status='insave').last()

    numb=""
    today = date.today()
    
    if  lastSv and 'save' in req.POST:
          
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
        if 'save' in req.POST:
            obj.prov_numb = 1
            numb = "I-{}-{}".format(today.strftime('%y-%m'), obj.prov_numb) 
    if lastIn and 'fin' in req.POST:
             
       
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
            
    return numb  
    



def statusInv(obj, req):
    """
    Function to save or finalise an invoice
    """
    if  'fin' in req.POST:
        obj.back_status = 'finished'
    elif  'save'in req.POST:
        obj.back_status = 'insave'
    return obj.back_status