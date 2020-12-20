from .models import *




def autoNumInvoice():
    """
    This function is made to make autonubers in every new invoice creted
    """
    
    lastIn = Invoices.objects.all().last()
    numb= ''
    l1= ['0','1','2','3','4','5','6','7','8','9']
    l = []
    if lastIn:
        l = [i for i in lastIn.number if i in l1]
        cleanNumb = int(''.join(l)) +1 
        numb = 'IN-'+str(cleanNumb)
    else:
        numb = 'IN-1'
    return numb



def autoNumQuote():
    """
    This function is made to make autonumbers in every new quote creted
    """
    
    lastIn = Quotes.objects.all().last()
    numb= ''
    l1= ['0','1','2','3','4','5','6','7','8','9']
    l = []
    if lastIn:
        l = [i for i in lastIn.number if i in l1]
        print(l)
        cleanNumb = int(''.join(l)) +1 
        numb = 'QU-'+str(cleanNumb)
    else:
        'QU-1'
    return numb