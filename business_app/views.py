from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView
from .forms import *
from django.contrib import messages


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

def UpdateSession(request, session_id):
    session = Session.objects.get(id=session_id)
    form = SessionForm(instance=session)

    if request.method == 'POST':
        form = SessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('session-detail', session_id)
    
    context={'form':form}
    return render(request, 'business_app/session_form.html', context)

def DeleteSession(request, session_id):
    session = Session.objects.get(id=session_id)

    if request.method == 'POST':
        session.delete()
        messages.success(request, "The session has been deleted.")

        return redirect('sessions')
    
    context = {'item': session, 'session_id':session_id}
    return render(request, 'business_app/session_confirm_delete.html', context)
