from django import forms
from .models import SongSinger

class SongSingerForm(forms.ModelForm):
    class Meta:
        model = SongSinger
        fields = ['Song', 'Singer']
