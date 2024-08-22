from django.db import models
from Songs.models import Song
from Writers.models import Writer

class SongWriter(models.Model):
    #SongWriterID = models.AutoField(primary_key=True)
    Song = models.ForeignKey(Song, on_delete=models.CASCADE)
    Writer= models.ForeignKey(Writer, on_delete=models.CASCADE)
    DateCreated = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('Song', 'Writer')
