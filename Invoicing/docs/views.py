from django.shortcuts import render
from .models import *
# Create your views here.



def home(request):
    invoices = Invoices.objects.filter(creator=request.user)
    quotes = Quotes.objects.filter(creator=request.user)
    context={
        "invoices": invoices,
        "quotes": quotes,
    }

    return render(request, 'docs/lists.html', context)