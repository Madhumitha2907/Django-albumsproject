from django.shortcuts import render, redirect
from .models import Passenger
from .forms import PassengerForm
from django.shortcuts import get_object_or_404

def passenger_new(request):
    if request.method == "POST":
        form = PassengerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('passenger_list')
    else:
        form = PassengerForm()
    return render(request, 'passenger_edit.html', {'form': form})

def passenger_list(request):
    passengers = Passenger.objects.all()
    return render(request, 'passenger_list.html', {'passengers': passengers})

def passenger_detail(request, pk):
    passenger = Passenger.objects.get(pk=pk)
    return render(request, 'passenger_detail.html', {'passenger': passenger})

def passenger_edit(request, pk):
    passenger = Passenger.objects.get(pk=pk)
    if request.method == "POST":
        form = PassengerForm(request.POST, instance=passenger)
        if form.is_valid():
            form.save()
            return redirect('passenger_list')
    else:
        form = PassengerForm(instance=passenger)
    return render(request, 'passenger_edit.html', {'form': form})

def home(request):
    return render(request, 'home.html')
def delete_passenger(request, pk):
    passenger = get_object_or_404(Passenger, pk=pk)
    if request.method == 'POST':
        passenger.delete()
        return redirect('passenger_list')
    return render(request, 'confirm_delete.html', {'passenger': passenger})
