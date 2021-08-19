import csv
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView
from .models import *



def home(request):
    return render(request, 'application/home.html')


def event(request):
    if request.method == 'POST':
        datetime = request.POST.get('datetime')
        organsier = request.POST.get('organsier')
        attendees = request.POST.get('attendees')
        department = request.POST.get('department')
        summary = request.POST.get('summary')
        purpose = request.POST.get('purpose')
        feedback = request.POST.get('feedback')

        if ((datetime == '') or (organsier == '') or (attendees == '') or (department == '') or (summary == '') or (
                purpose == '') or (feedback == '')):
            messages.info(request, "One or more fields are empty.")
            return redirect('Event')

        else:
            event = Event.objects.create(datetime=datetime, organsier=organsier, attendees=attendees,
                                         department=department, summary=summary, purpose=purpose, feedback=feedback)
            event.save()
            messages.info(request, "Event added Successfully.")
            return redirect('Event')
    else:
        return render(request, 'application/event.html')


def events(request):
    search = request.GET.get('search')
    if search is None:
        Events = Event.objects.all()
    else:
        Events = Event.objects.filter(
            Q(datetime__icontains=search) | Q(organsier__icontains=search) | Q(attendees__icontains=search)
            | Q(department__icontains=search) | Q(summary__icontains=search)
            | Q(purpose__icontains=search) | Q(feedback__icontains=search))
    return render(request, 'application/events.html', {'Events': Events})


def exportevents(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Date-Time', 'Organiser', 'Attendees', 'Department'
                     , 'Summary', 'Purpose', 'Feedback'])
    for event in Event.objects.all().values_list('datetime', 'organsier', 'attendees', 'department', 'summary', 'purpose', 'feedback'):
        writer.writerow(event)
    response['Content-Disposition'] = 'attachment; filename="EventsDetails.csv"'
    redirect('/events/')
    return response


def exportvisitors(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Date-Time', 'Visitor Name', 'To Meet', 'Department'
                     , 'Address', 'Purpose', 'Mobile No'])
    for visitor in Visitor.objects.all().values_list('datetime', 'visitorname', 'tomeet', 'department', 'address',
                                                     'purpose', 'mobile'):
        writer.writerow(visitor)
    response['Content-Disposition'] = 'attachment; filename="VisitorDetails.csv"'
    redirect('/visitors/')
    return response


def visitor(request):
    if request.method == 'POST':
        tomeet = request.POST.get('tomeet')
        visitorname = request.POST.get('visitor')
        department = request.POST.get('department')
        address = request.POST.get('address')
        purpose = request.POST.get('purpose')
        mobile = request.POST.get('mobile')
        if ((tomeet == '') or (visitorname == '') or (department == '') or (address == '') or (purpose == '') or (
                mobile == 0)):
            messages.info(request, "One or more fields are empty.")
            return redirect('Visitor')
        elif len(mobile) != 10:
            messages.info(request, "Enter valid 10 digit mobile number.")
            return redirect('Visitor')

        else:
            visitor = Visitor.objects.create(visitorname=visitorname, tomeet=tomeet, department=department,
                                             address=address, purpose=purpose, mobile=mobile)
            visitor.save()
            messages.info(request, "Visitor added Successfully.")
            return redirect('Visitor')
    else:
        return render(request, 'application/visitor.html')


def visitors(request):
    search = request.GET.get('search')
    if search is None:
        Visitors = Visitor.objects.all()
    else:
        Visitors = Visitor.objects.filter(
            Q(datetime__icontains= search) | Q(visitorname__icontains= search) | Q(tomeet__icontains= search)
            | Q(department__icontains= search) | Q(address__icontains= search)
            | Q(purpose__icontains= search) | Q(mobile__icontains= search))
    return render(request, 'application/visitors.html', {'Visitors': Visitors})


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
