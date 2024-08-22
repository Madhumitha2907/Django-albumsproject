from django.db import models
from Songs.models import Song
from choreographyids.models import ChoreographyID

class ChoreographyDetail(models.Model):
    ChoreographyDetailID = models.AutoField(primary_key=True)
    Song = models.ForeignKey(Song, on_delete=models.CASCADE)
    ChoreographyID = models.ForeignKey(ChoreographyID, on_delete=models.CASCADE)
    DateCreated = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('Song', 'ChoreographyID')
