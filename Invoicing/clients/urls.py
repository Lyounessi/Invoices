from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = "clients"


urlpatterns = [
    path("home/",  home, name="home"),
    path("create/",  CreateClient.as_view(), name="createClient"),# create and show client list
    #path("changeStat/<int:pk>",  actif, name="statChange"), # Change status to actif or inactif for a specific client
    path("details/<int:pk>",  ClientDetailsView.as_view(), name="detailsClient"), # view detail of a specific client
    path("update/<int:pk>",  clientUpdateView, name="updateClient"), # view detail of a specific client
    path("deactivate/<int:pk>",  deactivateClient, name="deactivateClient"), # view detail of a specific client

]