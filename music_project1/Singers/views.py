# singers/views.py

# Singers/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Singer
from .form import SingerForm  


def singer_list(request):
    singers = Singer.objects.all()
    return render(request, 'singers/singer_list.html', {'singers': singers})

def singer_detail(request, pk):
    singer = get_object_or_404(Singer, pk=pk)
    return render(request, 'singers/singer_detail.html', {'singer': singer})

def singer_create(request):
    if request.method == "POST":
        form = SingerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('singer_list')
    else:
        form = SingerForm()
    return render(request, 'singers/singer_form.html', {'form': form})

def singer_update(request, pk):
    singer = get_object_or_404(Singer, pk=pk)
    if request.method == "POST":
        form = SingerForm(request.POST, instance=singer)
        if form.is_valid():
            form.save()
            return redirect('singer_detail', pk=singer.pk)
    else:
        form = SingerForm(instance=singer)
    return render(request, 'singers/singer_form.html', {'form': form})

def singer_delete(request, pk):
    singer = get_object_or_404(Singer, pk=pk)
    if request.method == "POST":
        singer.delete()
        return redirect('singer_list')
    return render(request, 'singers/singer_confirm_delete.html', {'singer': singer})
