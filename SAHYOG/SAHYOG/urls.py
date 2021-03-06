#Import Dependencies
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    #Home
    path('',include('home.urls')),
    #Authentication
    path('',include('authentication.urls')),
    #Events
    path('',include('events.urls')),
    #Feralissues,
    path('',include('feralissues.urls')),
    #Donations
    path('',include('donations.urls')),
    #FirstAid
    path('',include('firstaid.urls')),
    #Adoptions
    path('',include('adoption.urls')),
    #Report
    path('',include('report.urls')),
]