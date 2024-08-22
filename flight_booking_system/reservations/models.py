from django.db import models
from flights.models import Flight
from passengers.models import Passenger

class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reservation {self.id} for {self.passenger.passenger_name}'
