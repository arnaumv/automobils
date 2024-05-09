from django.shortcuts import render

# Create your views here.
# A views.py
from django.shortcuts import render
from .models import Automobil

def llistat_automobils(request):
    automobils = Automobil.objects.all()
    return render(request, 'llistat_automobils.html', {'automobils': automobils})