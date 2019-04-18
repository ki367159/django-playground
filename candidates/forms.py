from django import forms
from .models import Candidate, Vote

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = '__all__'