from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
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

def root(request):
    return render(request, 'root.html')

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save
        login = (request, user)
        return redirect('root')

    return render(request, 'register.html', {'form': form})