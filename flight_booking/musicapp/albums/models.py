from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    date_created = models.DateField()
    date_updated = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='album_images/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("views_album", "Can view album"),  
            ("archive_album", "Can archive album"),  
            ("manage_album", "Can manage album"),  
        ]    

class Song(models.Model):
    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    duration = models.DurationField()
    date_created = models.DateField()
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("views_song", "Can view song"),  
            ("archive_song", "Can archive song"),  
            ("manage_song", "Can manage song"),  
        ]

class Singer(models.Model):
    name = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song, related_name='singers')
    date_created = models.DateField()
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        permissions = [
            ("views_singer", "Can view singer"), 
            ("archive_singer", "Can archive singer"),  
            ("manage_singer", "Can manage singer"),  
        ]

class Writer(models.Model):
    name = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song, related_name='writers')
    date_created = models.DateField()
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        permissions = [
            ("views_writer", "Can view writer"),  
            ("archive_writer", "Can archive writer"),  
            ("manage_writer", "Can manage writer"),  
        ]
