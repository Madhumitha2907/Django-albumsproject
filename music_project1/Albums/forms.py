from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['Title', 'ReleaseDate', 'Genre']
        widgets = {
            'ReleaseDate': forms.DateInput(attrs={'type': 'date'}),
            'DateCreated': forms.DateInput(attrs={'type': 'date', 'readonly': 'readonly'}),
            'DateUpdated': forms.DateInput(attrs={'type': 'date'})
        }
