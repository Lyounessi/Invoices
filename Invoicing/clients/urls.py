from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = "clients"


urlpatterns = [
    path("home/",  home, name="home"),
    path("create/",  CreateClient.as_view(), name="createClient"),

]