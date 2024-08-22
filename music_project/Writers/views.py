# writers/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Writer
from .form import WriterForm

def writer_list(request):
    writers = Writer.objects.all()
    return render(request, 'writers/writer_list.html', {'writers': writers})

def writer_detail(request, pk):
    writer = get_object_or_404(Writer, pk=pk)
    return render(request, 'writers/writer_detail.html', {'writer': writer})

def writer_create(request):
    if request.method == "POST":
        form = WriterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('writer_list')
    else:
        form = WriterForm()
    return render(request, 'writers/writer_form.html', {'form': form})

def writer_update(request, pk):
    writer = get_object_or_404(Writer, pk=pk)
    if request.method == "POST":
        form = WriterForm(request.POST, instance=writer)
        if form.is_valid():
            form.save()
            return redirect('writer_detail', pk=writer.pk)
    else:
        form = WriterForm(instance=writer)
    return render(request, 'writers/writer_form.html', {'form': form})

def writer_delete(request, pk):
    writer = get_object_or_404(Writer, pk=pk)
    if request.method == "POST":
        writer.delete()
        return redirect('writer_list')
    return render(request, 'writers/writer_confirm_delete.html', {'writer': writer})
