# Writers/forms.py

from django import forms
from .models import Writer

class WriterForm(forms.ModelForm):
    class Meta:
        model = Writer
        fields = ['Writer_Name']  # Include the fields you want to show in the form
        widgets = {
            'Writer_Name': forms.TextInput(attrs={'placeholder': 'Enter Writer Name'}),
        }
