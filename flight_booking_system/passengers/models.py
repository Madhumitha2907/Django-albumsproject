# models.py
from django.db import models

class Passenger(models.Model):
    passenger_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.passenger_name
