from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # Render the HTML template index.html with the
    # data in the context variable.
    return render ( request, 'business_app/index.html')


# example for a second login page with a basic placeholder response
def login(request):
    return render (HttpResponse, 'Login Page')