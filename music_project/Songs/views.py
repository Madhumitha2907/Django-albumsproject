from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound
from .models import Song
from .forms import SongForm

def song_list(request):
    try:
        songs = Song.objects.all()
        return render(request, 'songs/song-list.html', {'songs': songs})
    except Exception as e:
        return HttpResponseNotFound(f"Error: {e}")

def song_create(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongForm()
    return render(request, 'songs/song-form.html', {'form': form})

def song_update(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongForm(instance=song)
    return render(request, 'songs/song-form.html', {'form': form})

def song_delete(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        song.delete()
        return redirect('song_list')
    return render(request, 'songs/song-confirm-delete.html', {'song': song})
  
def song_detail(request, song_id):
    song = get_object_or_404(Song, SongID=song_id)
    return render(request, 'Songs/song_detail.html', {'song': song})
'''
def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    singer_url = reverse('singer_detail', args=[song.singer.pk])
    # Pass `singer_url` or use it as needed
    return render(request, 'Songs/song_detail.html', {'song': song})    '''

    