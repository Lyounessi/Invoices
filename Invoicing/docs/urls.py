from django.contrib import admin
from django.urls import path, include
from docs.view.invoices.views import * 
from docs.view.quotes.views import *
from .views import *




app_name = "docs"


urlpatterns = [
    path("list/",  home, name="home"),

    ################################## Invoices URLs ##################################
    
    path("createIn/",  CreateInvoice.as_view(), name="createInvoice"),
    path("detailsIn/<int:pk>",  InvoiceDetailsView.as_view(), name="detailsInvoice"), # view detail of a specific invoice
    path("deleteIn/<int:pk>",  InvoiceDeleteView.as_view(), name="deleteInvoice"), # delete a specific invoice
    path("updateIn/<int:pk>",  InvoiceUpdateView.as_view(), name="updateInvoice"), # update a specific invoice
    path("duplicate/<int:pk>",  dupInvoice, name="duplicateInvoice"), # update a specific invoice





    ################################## Quotes URLs ##################################
    
    path("createQu/",  CreateQuote.as_view(), name="createQuote"),
    path("detailsQu/<int:pk>",  QuoteDetailsView.as_view(), name="detailsQuote"), # view detail of a specific Quote
    path("deleteQu/<int:pk>",  QuoteDeleteView.as_view(), name="deleteQuote"), # delete a specific Quote
    path("updateQu/<int:pk>",  QuoteUpdateView.as_view(), name="updateQuote"), # update a specific Quote
    
]
