from django.forms import ModelForm
from .models import Session
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#create class for Session form
class SessionForm(ModelForm):
    class Meta:
        model = Session
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']