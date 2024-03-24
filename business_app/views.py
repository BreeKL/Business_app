from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView


# Create your views here.
def index(request):
    # Render the HTML template index.html with the
    # data in the context variable.
    return render ( request, 'business_app/index.html')


# example for a second login page with a basic placeholder response
def login(request):
    return render (HttpResponse, 'Login Page')


class SessionListView(ListView):
    model = Session