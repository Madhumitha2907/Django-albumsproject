from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=20,primary_key=True)
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    seat_availability = models.IntegerField()
