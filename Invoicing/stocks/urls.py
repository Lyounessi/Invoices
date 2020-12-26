from django.contrib import admin
from django.urls import path, include
from .views import *




app_name = "stocks"


urlpatterns = [
   path('home/', home, name='home'),
   path('addProd/', CreateProd.as_view(), name='createProd'),
   path('addServ/', CreateServ.as_view(), name='createServ'),
   path('detailProd/<int:pk>', ProdDetailsView.as_view(), name='details'),
]
