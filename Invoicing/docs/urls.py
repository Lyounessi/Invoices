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
    #path("deleteIn/<int:pk>",  InvoiceDeleteView.as_view(), name="deleteInvoice"), # delete a specific invoice
    path("saveInv/<int:pk>",saveInvoice, name="saveInv"),
    #path("updateIn/<int:pk>",  InvoiceUpdateView.as_view(), name="updateInvoice"), # update a specific invoice
    path("duplicate/<int:pk>",  dupInvoice, name="duplicateInvoice"), # update a specific invoice
    path("fin/<int:pk>",  finaliseInv, name="finaliseInvoice"), # finalise selected invoice
    path("unpaid_list/",  unpaidList, name="unpaidList"), # finalise selected invoice
    path("payments/<int:pk>",  payments, name="payInvoice"), # finalise selected invoice

    ################################## TRough PRoducts invoice URLs ##################################
    path('createIn/client/select/', selectClient, name='selectClient'),
    path("createIn/addprodInv/",  addPfromInv, name="addProds"), # AddProducts directly to the stock 
    path("createIn/selectprodInv/",  selecProd, name="selectProds"), # AddProducts to a selected invoice
    path("createIn/deleteArtInv/<int:pk>",  deleteArtFromInv, name="deleteArtInv"), # Delete a specific product
    path("createIn/addClientInv/",  addClientInv, name="addClientInv"), # Delete a specific product
    
    
    
    ################################## Quotes URLs ##################################
    
    path("createQt/",  CreateQuote.as_view(), name="createQuote"),
    path("detailsQt/<int:pk>",  QuoteDetailsView.as_view(), name="detailsQuote"), # view detail of a specific quote
    
    path("saveQt/<int:pk>",saveQuote, name="saveQuote"),
  
    path("duplicateQt/<int:pk>",  dupQuote, name="duplicateQuote"), # update a specific quote
    path("finQt/<int:pk>",  finaliseQuote, name="finaliseQuote"), # finalise selected quote
    

    ################################## TRough PRoducts Quotes URLs ##################################
    path('createQt/client/select/', selectClient, name='selectClient'),
    path("createQt/addprodQt/",  addPfromQuote, name="addProds"), # AddProducts directly to the stock 
    path("createQt/selectprodQt/",  selecProd, name="selectProds"), # AddProducts to a selected quote
    path("createQt/deleteArtQt/<int:pk>",  deleteArtFromQuote, name="deleteArtQuote"), # Delete a specific product
    path("createQt/addClientQt/",  addClientQuote, name="addClientQuote"), # Delete a specific product
]
