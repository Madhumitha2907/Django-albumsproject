from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation
from .forms import ReservationForm

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservation_list.html', {'reservations': reservations})

def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    return render(request, 'reservation_detail.html', {'reservation': reservation})

def reservation_new(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            return redirect('reservation_detail', pk=reservation.pk)
    else:
        form = ReservationForm()
    return render(request, 'reservation_edit.html', {'form': form})

def reservation_edit(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            reservation = form.save()
            return redirect('reservation_detail', pk=reservation.pk)
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservation_edit.html', {'form': form})
def reservation_delete(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.delete()
    return redirect('reservation_list')
def create_reservation(request):
    if request.method == 'POST':
        passenger_id = request.POST.get('passenger_id')
        flight_id = request.POST.get('flight_id')
        status = request.POST.get('status')
        flight = get_object_or_404(Flight, flight_number=flight_id)
        passenger = get_object_or_404(Passenger, id=passenger_id)

        if flight.seat_availability > 0:
            Reservation.objects.create(
                passenger=passenger,
                flight=flight,
                status=status
            )
            return redirect('reservation_success')
        else:
            return HttpResponse('No seats available')
    return render(request, 'create_reservation.html')

def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_cancelled')
    return render(request, 'cancel_reservation.html', {'reservation': reservation})
def reservations_view(request):
    # Get all reservations with their associated flight details (INNER JOIN)
    reservations = Reservation.objects.select_related('flight').all()
    return render(request, 'reservations.html', {'reservations': reservations})