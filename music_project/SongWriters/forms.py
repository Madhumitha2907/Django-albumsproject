from django import forms
from .models import SongWriter

class SongWriterForm(forms.ModelForm):
    class Meta:
        model = SongWriter
        fields = ['Song', 'Writer']
        widgets = {
            'DateCreated': forms.DateInput(attrs={'type': 'date', 'readonly': 'readonly'})
        }
