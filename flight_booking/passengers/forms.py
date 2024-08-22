from django import forms
from .models import Passenger

class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['passenger_name', 'email', 'contact_number']
