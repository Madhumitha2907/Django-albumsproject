from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound
from .models import SongSinger
from .forms import SongSingerForm

def song_singer_list(request):
    try:
        singers = SongSinger.objects.all()
        return render(request, 'songsingers/songsingers-list.html', {'singers': singers})
    except Exception as e:
        return HttpResponseNotFound(f"Error: {e}")

def song_singer_create(request):
    if request.method == 'POST':
        form = SongSingerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('song_singer_list')
    else:
        form = SongSingerForm()
    return render(request, 'songsingers/songsingers-form.html', {'form': form})

def song_singer_update(request, pk):
    singer = get_object_or_404(SongSinger, pk=pk)
    if request.method == 'POST':
        form = SongSingerForm(request.POST, instance=singer)
        if form.is_valid():
            form.save()
            return redirect('song_singer_list')
    else:
        form = SongSingerForm(instance=singer)
    return render(request, 'songsingers/songsingers-form.html', {'form': form})

def song_singer_delete(request, pk):
    singer = get_object_or_404(SongSinger, pk=pk)
    if request.method == 'POST':
        singer.delete()
        return redirect('song_singer_list')
    return render(request, 'songsingers/songsingers-confirm-delete.html', {'singer': singer})
