from .models import *
from datetime import date, datetime





def autoNumInvoice(obj, req):
    """
    This function is made to make autonubers in every new invoice creted
    """
    lastIn = Invoices.objects.filter(creator=req.user).last()
    numb=""
    today = date.today()
    if not lastIn:
        if  'save'in req.POST:
            obj.number = 1
            numb = "I-{}-{}".format(today.strftime('%y-%m'), obj.number) 
        elif 'fin' in req.POST:
          
            obj.number = 1
            numb = "{}-{}".format(today.strftime('%y-%m'), obj.number) 
        return numb
    idate = datetime.strptime(str(lastIn.dateCreation), '%Y-%m-%d')
    print('---------------------------------------------------->', idate)
    idate =  idate.date().strftime('%y-%m')
    if  'save'in req.POST:
        if idate == today.strftime('%y-%m') :
            obj.number = int(lastIn.number) + 1 # Increse number
            numb = "I-{}-{}".format(today.strftime('%y-%m'), obj.number) 
        else:   
            obj.number = 1
            numb = "I-{}-{}".format(today.strftime('%y-%m'), obj.number) 
        return numb    
    elif 'fin' in req.POST:
        if idate == today.strftime('%y-%m') :
            obj.number = int(lastIn.number) + 1 # Increse number
            numb = "{}-{}".format(today.strftime('%y-%m'), obj.number) 
        else:   
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