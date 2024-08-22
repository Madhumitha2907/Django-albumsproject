# albums/forms.py
from django import forms
from .models import Album, Song, Singer, Writer

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'release_date']

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'duration', 'album','date_created']

class SingerForm(forms.ModelForm):
    class Meta:
        model = Singer
        fields = ['name', 'songs','date_created']

class WriterForm(forms.ModelForm):
    class Meta:
        model = Writer
        fields = ['name', 'songs','date_created']
