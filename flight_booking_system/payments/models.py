from django.db import models
from tickets.models import Ticket

class Payment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f'Payment {self.id} for {self.ticket.id}'
