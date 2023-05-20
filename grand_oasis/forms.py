from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

class ReservationForm (ModelForm):
    class Meta:
        model = ReservationModel  
        fields = ["room", "checkin", "checkout"]
class UserForm (ModelForm):
    class Meta:
        model = User  
        fields = ["username", "email", "password"]
