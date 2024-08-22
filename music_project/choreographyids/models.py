from django.db import models

class ChoreographyID(models.Model):
    ChoreographyID = models.AutoField(primary_key=True)
    ChoreographyName = models.CharField(max_length=255)


    def __str__(self):
        return self.ChoreographyName
