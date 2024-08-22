from django.db import models
from Albums.models import Album

class Song(models.Model):
    SongID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Duration = models.TimeField()
    Album = models.ForeignKey(Album, on_delete=models.CASCADE)
    DateCreated = models.DateField(auto_now_add=True)
    DateUpdated = models.DateField(auto_now=True)
