from django.shortcuts import render, get_object_or_404, redirect
from .models import Payment
from .forms import PaymentForm

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment_list.html', {'payments': payments})

def payment_detail(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    return render(request, 'payment_detail.html', {'payment': payment})

def payment_new(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save()
            return redirect('payment_detail', pk=payment.pk)
    else:
        form = PaymentForm()
    return render(request, 'payment_edit.html', {'form': form})

def payment_edit(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == "POST":
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            payment = form.save()
            return redirect('payment_detail', pk=payment.pk)
    else:
        form = PaymentForm(instance=payment)
    return render(request, 'payment_edit.html', {'form': form})
