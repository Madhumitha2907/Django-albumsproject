from django.db import models

class Singer(models.Model):
    SingerID = models.AutoField(primary_key=True)
    Singer_Name = models.CharField(max_length=255)
  
    def __str__(self):
        return self.Singer_Name
