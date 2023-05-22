from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

class ReservationForm (ModelForm):
    class Meta:
        model = Reservation  
        fields = ["user", "room", "checkin", "checkout"]

class UserForm (ModelForm):
    class Meta:
        model = User  
        fields = ["username", "email", "password"]

class ContactForm (ModelForm):
    class Meta:
        model = Contact  
        fields = ["msg_sender", "msg_receiver", "subject", "message"]

class DateForm (ModelForm):
    class Meta:
        model = ServiceDate  
        fields = "__all__"
