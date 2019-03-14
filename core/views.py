from django.http import HttpResponse
from django.shortcuts import render
from .forms import BmiForm

def hello(request):
    return HttpResponse('Helli World!')

def bmi(request):
    form = BmiForm(request.POST or None)
    if form.is_valid():
        h = form.cleaned_data['h']
        w = form.cleaned_data['w']
        bmi = w / (h ** 2)
        return render(request, 'bmi.html', {'bmi': bmi})
    
    return render(request, 'bmi-input.html', {'form': form})

