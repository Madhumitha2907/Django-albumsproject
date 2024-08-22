from django.db import models
from Songs.models import Song
from Singers.models import Singer

class SongSinger(models.Model):
    #SongSingerID = models.AutoField(primary_key=True)
    Song = models.ForeignKey(Song, on_delete=models.CASCADE)
    Singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    

    class Meta:
        unique_together = ('Song', 'Singer')
