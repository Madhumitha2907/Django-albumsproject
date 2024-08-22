from django.db import models
from reservations.models import Reservation

class Ticket(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=5)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Ticket {self.id} for {self.reservation.passenger.passenger_name}'
