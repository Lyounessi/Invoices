from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views import View
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required


def home(request):
    """
    A test home users View before log in
    """
    return render(request, 'users/home.html')


@login_required(login_url='/user/logs/login/')
def dashboard(request):
    """
    this view present a dashboard of user after login
    """
    return render(request, 'dashboard/index.html')


def create_user(request):
    """
    this view is dedicated to create user account as signup
    """
    if request.method == "POST":
        
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            
            return redirect('users:home')
        else:
            messages.error(request, 'The form is invalid.')
        
    else:

        form = SignUpForm()

    return render(request, 'registration/signup.html', {"form": form})


