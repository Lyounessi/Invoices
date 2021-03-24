from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth import views




app_name = "users"


urlpatterns = [
    path("register/",  create_user, name="register"),
    path("home/",  home, name="home"),
    path('logs/', include('django.contrib.auth.urls')),
    path('dashboard/', dashboard, name="dashindex"),

    path('login/',views.LoginView.as_view(
        template_name="registration/login.html",
        authentication_form=UserLoginForm
        ),
        name='login'),
    
    ######### Company's URLs ##########

    path('company_create/', CreateCompany.as_view(), name='companyCreate'),#create companys
    path('company/<int:pk>', CompanyDetailView.as_view(), name='companyDetail'),# view details of company
    path('company/<int:pk>/update', CompanyUpdateView.as_view(), name='companyUpdate'),# update company's infos
    path('company/<int:pk>/delete', CompanyDeleteView.as_view(), name='companyDelete'),#delete company
    
]


