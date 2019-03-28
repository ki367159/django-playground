from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Candidate
from .forms import CandidateForm
from core.forms import DeleteConfirmForm

def index(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidates/index.html',{
        'candidates': candidates,
    })

def add(request):
    form = CandidateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, '新增成功')
        return redirect('/candidates/')
    return render(request, 'candidates/add.html', {
        'form': form,
    })

def edit(request, pk):
    # candidate = Candidate.objects.get(pk=pk)
    candidate = get_object_or_404(Candidate, pk=pk)
    form = CandidateForm(request.POST or None, instance=candidate)
    if form.is_valid():
        form.save()
        messages.success(request, '編輯成功')
        return redirect('/candidates/')
    return render(request, 'candidates/edit.html', {
        'form': form,
    })

def delete(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid():
        candidate.delete()
        messages.success(request, '刪除成功')
        return redirect('/candidates/')
    return render(request, 'candidates/delete.html', {
        'form': form,
    })

def show(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    return render(request, 'candidates/show.html', {
        'candidate': candidate,
    })