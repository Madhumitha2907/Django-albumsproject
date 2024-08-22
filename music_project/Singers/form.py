# Singers/forms.py

from django import forms
from .models import Singer

class SingerForm(forms.ModelForm):
    class Meta:
        model = Singer
        fields = ['Singer_Name']
        widgets = {
            'Singer_Name': forms.TextInput(attrs={'placeholder': 'Enter Singer Name'}),
        }
