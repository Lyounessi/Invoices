from django.contrib import admin  
from django.urls import path, include
from .views import *




app_name = "reminders"


urlpatterns = [
    
    path("list_reminders/",  listOfTexts, name="listReminders"),
    path("update/<int:pk>",  TextUpdate.as_view(), name="updateText"), # view detail of a specific client

    path("create_reminder/",  CreateServ.as_view(), name="createReminders"),
]
