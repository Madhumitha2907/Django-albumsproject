from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from flights.models import Flight
from passengers.models import Passenger

class Reservation(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, related_name='reservations', on_delete=models.CASCADE)
    reservation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,default="Confirmed")  # 'Reserved', 'Cancelled', etc.

    def __str__(self):
        return f'Reservation {self.id} for {self.passenger} on {self.flight}'

@receiver(post_save, sender=Reservation)
def update_seat_availability_on_save(sender, instance, created, **kwargs):
    if created:
        instance.flight.decrease_seat_availability()

@receiver(post_delete, sender=Reservation)
def update_seat_availability_on_delete(sender, instance, **kwargs):
    instance.flight.increase_seat_availability()
