from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Session(models.Model):

    #List of choices for major value in database, human readable name
    LENGTH = (
    ('30', '30 minute session'),
    ('45', '45 minute session'),
    ('60', '60 minute session'),
    ('75', '75 minute session'),
    ('90', '90 minute session'),
    ('120', '120 minute session'),
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    length = models.CharField(max_length=20, choices=LENGTH)
    price = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10000)])
    is_active = models.BooleanField()

    # For creating a user account
    # user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.name

    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('session-detail', args=[str(self.id)])
 
class CalendarEvent(models.Model):

    name = models.CharField(max_length=200)

    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    def __str__(self):
        return self.name