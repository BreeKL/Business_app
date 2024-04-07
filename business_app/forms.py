from django.forms import ModelForm
from .models import Session
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


#create class for Session form
class SessionForm(ModelForm):
    class Meta:
        model = Session
        fields = '__all__'
