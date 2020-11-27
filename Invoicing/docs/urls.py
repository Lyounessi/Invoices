from django.contrib import admin
from django.urls import path, include
from docs.view.invoices.views import * 
from docs.view.quotes.views import *




app_name = "docs"


urlpatterns = [
    ################################## Invoices URLs ##################################
    
    path("create/",  CreateInvoice.as_view(), name="createInvoice"),




    ################################## Quotes URLs ##################################

  
    
]
