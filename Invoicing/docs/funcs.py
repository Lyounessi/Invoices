from .models import *
from datetime import date, datetime





def autoNumInvoice(obj, req):
    """
    This function is made to make autonubers in every new invoice creted
    """
    lastIn = Invoices.objects.all().last()
    numb=""
    if lastIn:
        idate = datetime.strptime(str(lastIn.dateCreation), '%Y-%m-%d')
        idate =  idate.date().strftime('%y-%M')
        today = date.today()

        if  'save'in req.POST:
            if idate == today.strftime('%y-%M') :
                obj.number = int(lastIn.number) + 1 # Increse number
                numb = "I-{}-{}".format(today.strftime('%y-%M'), obj.number) 
            else:   
                obj.number = 1
                numb = "I-{}-{}".format(today.strftime('%y-%M'), obj.number) 
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