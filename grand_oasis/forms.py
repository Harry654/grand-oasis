from django.forms import ModelForm
from .models import *


class RegistrationForm (ModelForm):
    class Meta:
        model = ClientRegisterModel  
        fields = "__all__"

class LoginForm (ModelForm):
    class Meta:
        model = ClientLoginModel  
        fields = "__all__"
