from django import forms
from .models import ChoreographyID

class ChoreographyIDForm(forms.ModelForm):
    class Meta:
        model = ChoreographyID
        fields = ['ChoreographyName']
