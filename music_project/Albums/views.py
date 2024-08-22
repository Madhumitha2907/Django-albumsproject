from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound
from .models import Album
from .forms import AlbumForm

def album_list(request):
    try:
        albums = Album.objects.all()
        return render(request, 'albums/album-list.html', {'albums': albums})
    except Exception as e:
        return HttpResponseNotFound(f"Error: {e}")

def album_create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request, 'albums/album-form.html', {'form': form})

def album_update(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'albums/album-form.html', {'form': form})

def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect('album_list')
    return render(request, 'albums/album-confirm-delete.html', {'album': album})
def home(request):
    return render(request, 'home.html')
def album_detail(request, album_id):
    #album = get_object_or_404(Album, id=album_id)
    album = get_object_or_404(Album, AlbumID=album_id)

    return render(request, 'albums/album_detail.html', {'album': album})
def song_detail(request, song_id):
    song = get_object_or_404(Song, SongID=song_id)
    return render(request, 'Songs/song_detail.html', {'song': song})    