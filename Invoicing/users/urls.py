from django.contrib import admin
from django.urls import path, include
from .views import *



app_name = "users"


urlpatterns = [
    path("register/",  create_user, name="register"),
    path("home/",  home, name="home"),
    path('logs/', include('django.contrib.auth.urls')),
    path('dashboard/', dashboard, name="dashindex"),

    
]



#FOR logs URLs
"""
    accounts/login/ [name='login']
    accounts/logout/ [name='logout']
    accounts/password_change/ [name='password_change']
    accounts/password_change/done/ [name='password_change_done']
    accounts/password_reset/ [name='password_reset']
    accounts/password_reset/done/ [name='password_reset_done']
    accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    accounts/reset/done/ [name='password_reset_complete']
    """