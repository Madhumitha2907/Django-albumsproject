from django.shortcuts import render, get_object_or_404, redirect
from .models import Album, Song, Singer, Writer
from .forms import AlbumForm, SongForm, SingerForm, WriterForm

# Home page showing all albums
def album_list(request):
    albums = Album.objects.all()
    return render(request, 'albums/album_list.html', {'albums': albums})

# Album details page showing all songs in the album
def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    songs = album.songs.all()
    return render(request, 'albums/album_detail.html', {'album': album, 'songs': songs})

# Song details page showing singers and writers
def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    singers = song.singers.all()
    writers = song.writers.all()
    return render(request, 'songs/song_detail.html', {'song': song, 'singers': singers, 'writers': writers})

# Add, edit, delete views for Album, Song, Singer, Writer
def album_add(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request, 'albums/album_form.html', {'form': form})

def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_detail', pk=pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'albums/album_form.html', {'form': form})

def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect('album_list')
    return render(request, 'albums/album_confirm_delete.html', {'album': album})

# Similar views for Song
def song_add(request):
    if request.method == "POST":
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save()
            return redirect('song_detail', pk=song.pk)
    else:
        form = SongForm()
    return render(request, 'songs/song_form.html', {'form': form})

def song_edit(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == "POST":
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return redirect('song_detail', pk=pk)
    else:
        form = SongForm(instance=song)
    return render(request, 'songs/song_form.html', {'form': form})

def song_delete(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == "POST":
        song.delete()
        return redirect('album_detail', pk=song.album.pk)
    return render(request, 'songs/song_confirm_delete.html', {'song': song})

# Similar views for Singer
def singer_add(request):
    if request.method == "POST":
        form = SingerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('singer_list')
    else:
        form = SingerForm()
    return render(request, 'singers/singer_form.html', {'form': form})

def singer_edit(request, pk):
    singer = get_object_or_404(Singer, pk=pk)
    if request.method == "POST":
        form = SingerForm(request.POST, instance=singer)
        if form.is_valid():
            form.save()
            return redirect('singer_detail', pk=pk)
    else:
        form = SingerForm(instance=singer)
    return render(request, 'singers/singer_form.html', {'form': form})

def singer_delete(request, pk):
    singer = get_object_or_404(Singer, pk=pk)
    if request.method == "POST":
        singer.delete()
        return redirect('singer_list')
    return render(request, 'singers/singer_confirm_delete.html', {'singer': singer})

# Similar views for Writer
def writer_add(request):
    if request.method == "POST":
        form = WriterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('writer_list')
    else:
        form = WriterForm()
    return render(request, 'writers/writer_form.html', {'form': form})

def writer_edit(request, pk):
    writer = get_object_or_404(Writer, pk=pk)
    if request.method == "POST":
        form = WriterForm(request.POST, instance=writer)
        if form.is_valid():
            form.save()
            return redirect('writer_detail', pk=pk)
    else:
        form = WriterForm(instance=writer)
    return render(request, 'writers/writer_form.html', {'form': form})

def writer_delete(request, pk):
    writer = get_object_or_404(Writer, pk=pk)
    if request.method == "POST":
        writer.delete()
        return redirect('writer_list')
    return render(request, 'writers/writer_confirm_delete.html', {'writer': writer})
def singer_detail(request, pk):
    singer = get_object_or_404(Singer, pk=pk)
    return render(request, 'singers/singer_detail.html', {'singer': singer})
def writer_detail(request, pk):
    writer = get_object_or_404(Writer, pk=pk)
    return render(request, 'writers/writer_detail.html', {'writer': writer})
def add_singer_to_song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    if request.method == 'POST':
        form = SingerForm(request.POST)
        if form.is_valid():
            singer = form.save()
            song.singers.add(singer)
            return redirect('song_detail', pk=song_id)
    else:
        form = SingerForm()
    return render(request, 'singers/singer_form.html', {'form': form})
def add_writer_to_song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    if request.method == 'POST':
        form = WriterForm(request.POST)
        if form.is_valid():
            writer = form.save()
            song.writers.add(writer)
            return redirect('song_detail', pk=song_id)
    else:
        form = WriterForm()
    return render(request, 'writers/writer_form.html', {'form': form})    

def singer_list(request):
    singers = Singer.objects.all().distinct()
    return render(request, 'singers/singer_list.html', {'singers': singers})
def writer_list(request):
    writers= Writer.objects.all().distinct()
    return render(request, 'writers/writer_list.html', {'writers': writers})
