from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=20,primary_key=True)
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    seat_availability = models.IntegerField()
    base_cost = models.DecimalField(max_digits=10, decimal_places=2,default=5500.67) 
    def decrease_seat_availability(self):
        if self.seat_availability > 0:
            self.seat_availability -= 1
            self.save()

    def increase_seat_availability(self):
        self.seat_availability += 1
        self.save()
    def update_ticket_and_payment(sender, instance, **kwargs):
        from .ticket import Ticket  # Import locally to avoid circular import
        tickets = Ticket.objects.filter(flight=instance)
        for ticket in tickets:
            ticket.ticket_price = instance.base_cost
            ticket.save()

        if hasattr(ticket, 'payment'):
            payment = ticket.payment
            payment.amount = ticket.ticket_price
            payment.save()
    
