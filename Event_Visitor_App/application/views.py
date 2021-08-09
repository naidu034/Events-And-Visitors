from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .models import *



def home(request):
    return render(request, 'application/home.html')


def event(request):
    return render(request, 'application/event.html')

def events(request):
    return render(request, 'application/events.html')

def visitor(request):
    return render(request, 'application/visitor.html')

def visitors(request):
    return render(request, 'application/visitors.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/home')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('/')
    else:
        return render(request, 'application/login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')