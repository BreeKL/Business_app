from django.urls import path
from . import views

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
path('login/', views.login, name='login'),
path('sessions/', views.SessionListView.as_view(), name='sessions'),
path('session/<pk>', views.SessionDetailView.as_view(), name='session-detail'),

path('session/create/', views.CreateSession, name='create-session'),
path('session/<session_id>/update/', views.UpdateSession, name='update-session'),

]
