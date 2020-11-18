from django.contrib import admin
from django.urls import path, include
from .views import *



app_name = "users"


urlpatterns = [
    path("register/",  create_user, name="register"),
    path("home/",  home, name="home"),
    path('logs/', include('django.contrib.auth.urls')),
    path('dashboard/', dashboard, name="dashindex"),

    ######### Company's URLs ##########

    path('company_create/', CreateCompany.as_view(), name='companyCreate'),#create companys
    path('company/<int:pk>', CompanyDetailView.as_view(), name='companyDetail'),# view details of company
    path('company/<int:pk>/update', CompanyUpdateView.as_view(), name='companyUpdate'),# update company's infos
    path('company/<int:pk>/delete', CompanyDeleteView.as_view(), name='companyDelete'),#delete company
    
]



#FOR logs URLs
"""
    user/logs/login/ [name='login']
    user/logs/logout/ [name='logout']
    user/logs/password_change/ [name='password_change']
    user/logs/password_change/done/ [name='password_change_done']
    user/logs/password_reset/ [name='password_reset']
    user/logs/password_reset/done/ [name='password_reset_done']
    user/logs/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    user/logs/reset/done/ [name='password_reset_complete']
    """