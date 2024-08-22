from django import forms
from .models import Song

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['Title', 'Duration', 'Album']
        widgets = {
            'Duration': forms.TimeInput(attrs={'type': 'time'}),
            'DateCreated': forms.DateInput(attrs={'type': 'date', 'readonly': 'readonly'}),
            'DateUpdated': forms.DateInput(attrs={'type': 'date'})
        }
