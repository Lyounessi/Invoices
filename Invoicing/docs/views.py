from django.shortcuts import render
from .models import *
# Create your views here.



def home(request):
    invoices = Invoices.objects.all()
    quotes = Quotes.objects.all()
    context={
        "invoices": invoices,
        "quotes": quotes,
    }

    return render(request, 'docs/lists.html', context)