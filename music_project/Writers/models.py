from django.db import models

class Writer(models.Model):
    WriterID = models.AutoField(primary_key=True)
    Writer_Name = models.CharField(max_length=255)
    

    def __str__(self):
        return self.Writer_Name
