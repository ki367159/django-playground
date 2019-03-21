from django.contrib import admin
from .models import Candidate

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    search_fields = [ 'name', 'politics' ]
    list_display = [ 'name', 'age' ]