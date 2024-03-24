from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView
from .forms import *


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

class SessionDetailView(DetailView):
    model = Session


def CreateSession(request):

    form = SessionForm()

    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sessions')
        
    context={'form':form}
    return render(request, 'business_app/session_form.html', context)
