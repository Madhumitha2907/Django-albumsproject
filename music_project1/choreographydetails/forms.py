from django import forms
from .models import ChoreographyDetail

class ChoreographyDetailForm(forms.ModelForm):
    class Meta:
        model = ChoreographyDetail
        fields = ['Song', 'ChoreographyID']
        widgets = {
            'DateCreated': forms.DateInput(attrs={'type': 'date', 'readonly': 'readonly'})
        }
