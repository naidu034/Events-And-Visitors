from django.urls import path
from . import views


urlpatterns =[
    path('', views.login, name='Login'),
    path('home/', views.home, name='Home'),
    path('visitor/', views.visitor, name='Visitor'),
    path('visitors/', views.visitors, name='Visitors'),
    path('event/', views.event, name='Event'),
    path('events/', views.events, name='Events'),
    path('logout/', views.logout, name='Logout'),
    path('exportevents/', views.exportevents, name='ExportEvents'),
    path('exportvisitors/', views.exportvisitors, name='ExportVisitors'),
]