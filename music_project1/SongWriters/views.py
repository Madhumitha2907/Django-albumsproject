from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound
from .models import SongWriter
from .forms import SongWriterForm

def song_writer_list(request):
    try:
        writers = SongWriter.objects.all()
        return render(request, 'songwriters/songwriters-list.html', {'writers': writers})
    except Exception as e:
        return HttpResponseNotFound(f"Error: {e}")

def song_writer_create(request):
    if request.method == 'POST':
        form = SongWriterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('song_writer_list')
    else:
        form = SongWriterForm()
    return render(request, 'songwriters/songwriters-form.html', {'form': form})

def song_writer_update(request, pk):
    writer = get_object_or_404(SongWriter, pk=pk)
    if request.method == 'POST':
        form = SongWriterForm(request.POST, instance=writer)
        if form.is_valid():
            form.save()
            return redirect('song_writer_list')
    else:
        form = SongWriterForm(instance=writer)
    return render(request, 'songwriters/songwriters-form.html', {'form': form})

def song_writer_delete(request, pk):
    writer = get_object_or_404(SongWriter, pk=pk)
    if request.method == 'POST':
        writer.delete()
        return redirect('song_writer_list')
    return render(request, 'songwriters/songwriters-confirm-delete.html', {'writer': writer})
