from django.shortcuts import render, get_object_or_404, redirect
from .models import Flight
from reservations.models import Reservation
from .forms import FlightForm
from django.db.models import Count


def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'flight_list.html', {'flights': flights})

def flight_detail(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    return render(request, 'flight_detail.html', {'flight': flight})

def flight_new(request):
    if request.method == "POST":
        form = FlightForm(request.POST)
        if form.is_valid():
            flight = form.save()
            return redirect('flight_detail', pk=flight.pk)
    else:
        form = FlightForm()
    return render(request, 'flight_edit.html', {'form': form})

def flight_edit(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    if request.method == "POST":
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            flight = form.save()
            return redirect('flight_detail', pk=flight.pk)
    else:
        form = FlightForm(instance=flight)
    return render(request, 'flight_edit.html', {'form': form})
def flight_delete(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    flight.delete()
    return redirect('flight_list')
'''    
def flights_view(request):
    # Get all flights and their reservations (LEFT JOIN)
    flights = Flight.objects.prefetch_related('reservations').all()
    return render(request, 'flights.html', {'flights': flights})    
    '''
def flights_view(request):
    flights_with_reservation_count = Flight.objects.annotate(num_reservations=Count('reservations'))

    flight_data = []
    for flight in flights_with_reservation_count:
        if flight.num_reservations > 0:
            reservations = Reservation.objects.prefetch_related('flight')
            for reservation in reservations:
                flight_data.append({
                    'flight_number': flight.flight_number,
                    'passenger_name': reservation.passenger.passenger_name
                })
        else:
            flight_data.append({
                'flight_number': flight.flight_number,
                'passenger_name': 'No Reservations'
            })
    
    context = {'flights': flight_data}
    return render(request, 'flights.html', context)    