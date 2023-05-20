from django.forms import ModelForm
from .models import *


class RegistrationForm (ModelForm):
    class Meta:
        model = ClientModel  
        fields = "__all__"

class LoginForm (ModelForm):
    class Meta:
        model = ClientLoginModel  
        fields = "__all__"

class ReservationForm (ModelForm):
    class Meta:
        model = ReservationModel  
        fields = "__all__"
