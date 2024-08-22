from django.shortcuts import render, get_object_or_404, redirect
from .models import Flight
from .forms import FlightForm

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
