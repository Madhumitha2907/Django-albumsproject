from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound
from .models import ChoreographyID
from .forms import ChoreographyIDForm

def choreography_id_list(request):
    try:
        ids = ChoreographyID.objects.all()
        return render(request, 'choregraphyids/choregraphyid-details.html', {'ids': ids})
    except Exception as e:
        return HttpResponseNotFound(f"Error: {e}")

def choreography_id_create(request):
    if request.method == 'POST':
        form = ChoreographyIDForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('choreography_id_list')
    else:
        form = ChoreographyIDForm()
    return render(request, 'choregraphyids/choregraphyid-form.html', {'form': form})

def choreography_id_update(request, pk):
    choreo_id = get_object_or_404(ChoreographyID, pk=pk)
    if request.method == 'POST':
        form = ChoreographyIDForm(request.POST, instance=choreo_id)
        if form.is_valid():
            form.save()
            return redirect('choreography_id_list')
    else:
        form = ChoreographyIDForm(instance=choreo_id)
    return render(request, 'choregraphyids/choregraphyid-form.html', {'form': form})

def choreography_id_delete(request, pk):
    choreo_id = get_object_or_404(ChoreographyID, pk=pk)
    if request.method == 'POST':
        choreo_id.delete()
        return redirect('choreography_id_list')
    return render(request, 'choregraphyids/choregraphyid-confirm-delete.html', {'choreo_id': choreo_id})
