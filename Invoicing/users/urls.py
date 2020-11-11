from django.contrib import admin
from django.urls import path
from .views import *


app_name = "users"


urlpatterns = [
    path("register/",  create_user, name="register"),
    path("home/",  home, name="home"),

]