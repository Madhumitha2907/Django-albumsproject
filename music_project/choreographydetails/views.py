from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound
from .models import ChoreographyDetail
from .forms import ChoreographyDetailForm

def choreography_detail_list(request):
    try:
        details = ChoreographyDetail.objects.all()
        return render(request, 'choregraphydetails/choregraphydetails-list.html', {'details': details})
    except Exception as e:
        return HttpResponseNotFound(f"Error: {e}")

def choreography_detail_create(request):
    if request.method == 'POST':
        form = ChoreographyDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('choreography_detail_list')
    else:
        form = ChoreographyDetailForm()
    return render(request, 'choregraphydetails/choregraphydetails-form.html', {'form': form})

def choreography_detail_update(request, pk):
    detail = get_object_or_404(ChoreographyDetail, pk=pk)
    if request.method == 'POST':
        form = ChoreographyDetailForm(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return redirect('choreography_detail_list')
    else:
        form = ChoreographyDetailForm(instance=detail)
    return render(request, 'choregraphydetails/choregraphydetails-form.html', {'form': form})

def choreography_detail_delete(request, pk):
    detail = get_object_or_404(ChoreographyDetail, pk=pk)
    if request.method == 'POST':
        detail.delete()
        return redirect('choreography_detail_list')
    return render(request, 'choregraphydetails/choregraphydetails-confirm-delete.html', {'detail': detail})
