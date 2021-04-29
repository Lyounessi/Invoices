from django.shortcuts import render
from docs.models import * 
from .funcs import * 
# Create your views here.

def dash(request):
    '''
    custum dashboard
    '''
    #total Invoices
    total_invoices = Invoices.objects.all()
    total_invoices = total_invoices.count()
    #total Unpaid invoices
    unpaid = Invoices.objects.filter(creator=request.user, stats='notPayed', back_status='Finilised')
    unpaid = unpaid.count()
    # total amount still to pay
    part_paid = Invoices.objects.filter(creator=request.user, stats='partial payed', back_status='Finilised')
    count = 0
    for elt in part_paid:
        count += elt.still_to_pay
    
    # total amount 
    total = Invoices.objects.filter(creator=request.user, stats='partial payed', back_status='Finilised')
    count_total = 0
    for elt in part_paid:
        count_total += elt.total
    

    context ={
        'total_invoices': total_invoices,
        'unpaid': unpaid,
        'part_paid': count,
        'total_cash' : count_total,
        

    }

    return render(request, 'dashboard/dash.html', context)