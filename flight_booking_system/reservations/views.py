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
