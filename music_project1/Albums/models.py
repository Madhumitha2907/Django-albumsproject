
from django.db import models

class Album(models.Model):
    AlbumID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    ReleaseDate = models.DateField()
    Genre = models.CharField(max_length=100)
    DateCreated = models.DateField(auto_now_add=True)
    DateUpdated = models.DateField(auto_now=True)
