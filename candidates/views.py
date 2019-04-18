from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Candidate
from .forms import CandidateForm, VoteForm
from core.forms import DeleteConfirmForm


@login_required
def index(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidates/index.html',{
        'candidates': candidates,
    })

@login_required
def add(request):
    form = CandidateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        candidate = form.save()
        messages.success(request, '新增成功')
        return redirect('candidates:show', pk=candidate.pk)
    return render(request, 'candidates/add.html', {
        'form': form,
    })

@login_required
def edit(request, pk):
    # candidate = Candidate.objects.get(pk=pk)
    candidate = get_object_or_404(Candidate, pk=pk)
    form = CandidateForm(request.POST or None, request.FILES or None, instance=candidate)
    if form.is_valid():
        candidate = form.save()
        messages.success(request, '編輯成功')
        return redirect('candidates:show', pk=candidate.pk)
    return render(request, 'candidates/edit.html', {
        'form': form,
    })


@login_required
def delete(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid():
        candidate.delete()
        messages.success(request, '刪除成功')
        return redirect('candidates:show', pk=candidate.pk)
    return render(request, 'candidates/delete.html', {
        'form': form,
    })


@login_required
def show(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    return render(request, 'candidates/show.html', {
        'candidate': candidate,
    })

@login_required
def vote(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    form = VoteForm({'candidate': candidate.pk, 'user': request.user.pk})
    if form.is_valid():
        messages.success(request, 'Vote success')
        form.save()
    else:
        messages.warning(request, form.errors)

    return redirect('candidates:index')