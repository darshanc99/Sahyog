#Import Dependencies
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
	return redirect('sahyog')