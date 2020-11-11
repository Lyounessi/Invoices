from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views import View
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    return render(request, 'users/home.html')
    



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

    return render(request, 'users/signup.html', {"form": form})