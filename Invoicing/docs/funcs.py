from .models import *




def autoNumInvoice():
    """
    This function is made to make autonubers in every new invoice creted
    """
    
    lastIn = Invoices.objects.all().last()
    numb= ''
    if lastIn :
        numb = int(lastIn.number) + 1
    else:
        numb = 1

    return numb



def autoNumQuote():
    """
    This function is made to make autonumbers in every new quote creted
    """
    
    lastIn = Quotes.objects.all().last()
    numb= ''
    if lastIn :
        numb = int(lastIn.number) + 1
    else:
        numb = 1

    return numb