# albums/models.py
from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class Song(models.Model):
    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    duration = models.DurationField()
    date_created = models.DateField()
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class Singer(models.Model):
    name = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song, related_name='singers')
    date_created = models.DateField()
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Writer(models.Model):
    name = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song, related_name='writers')
    date_created = models.DateField()
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
