from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = "clients"


urlpatterns = [
    path("home/",  home, name="home"),
    path("create/",  CreateClient.as_view(), name="createClient"),# create and show client list
    path("delete/<int:pk>",  ClientDeleteView.as_view(), name="deleteClient"), # delete a specific client
    path("details/<int:pk>",  ClientDetailsView.as_view(), name="detailsClient"), # view detail of a specific client
    path("update/<int:pk>",  ClientUpdateView.as_view(), name="updateClient"), # view detail of a specific client

    


]