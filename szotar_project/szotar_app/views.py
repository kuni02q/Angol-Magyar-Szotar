# szotar_app/views.py

from django.shortcuts import render, redirect
from .models import Szopar
from django.urls import reverse
import random
def index(request):
    return render(request, 'index.html')
def add_szopar(request):
    if request.method == 'POST':
        magyar = request.POST.get('magyar')
        angol = request.POST.get('angol')
        if magyar and angol and len(magyar) <= 80 and len(angol) <= 80:
            Szopar.objects.create(magyar=magyar, angol=angol)
            return redirect('list_szoparok')
        else:
            error = "Hibás adatok! Kérjük, ellenőrizd a bevitt adatokat."
            return render(request, 'add_szopar.html', {'error': error})
    return render(request, 'add_szopar.html')
def list_szoparok(request):
    szoparok = Szopar.objects.all()
    return render(request, 'list_szoparok.html', {'szoparok': szoparok})
def practice(request):
    if request.method == 'POST':
        try:
            kerdesek_szama = int(request.POST.get('kerdesek_szama'))
        except ValueError:
            kerdesek_szama = 5  # Alapértelmezett
        szoparok = list(Szopar.objects.all())
        if not szoparok:
            error = "A szótár üres! Először adj hozzá szavakat."
            return render(request, 'practice.html', {'error': error})
        if kerdesek_szama > len(szoparok):
            kerdesek_szama = len(szoparok)
        kerdesek = random.sample(szoparok, kerdesek_szama)
        request.session['kerdesek'] = [szopar.id for szopar in kerdesek]
        return redirect('quiz')
    return render(request, 'practice.html')
def quiz(request):
    if 'kerdesek' not in request.session:
        return redirect('practice')
    kerdesek_ids = request.session['kerdesek']
    kerdesek = Szopar.objects.filter(id__in=kerdesek_ids)
    if request.method == 'POST':
        valaszok = {}
        for szopar in kerdesek:
            valasz = request.POST.get(str(szopar.id))
            valaszok[szopar.id] = valasz
        request.session['valaszok'] = valaszok
        return redirect('results')
    return render(request, 'quiz.html', {'kerdesek': kerdesek})
def results(request):
    if 'kerdesek' not in request.session or 'valaszok' not in request.session:
        return redirect('practice')
    kerdesek_ids = request.session['kerdesek']
    valaszok = request.session['valaszok']
    kerdesek = Szopar.objects.filter(id__in=kerdesek_ids)
    eredmenyek = []
    for szopar in kerdesek:
        adott_valasz = valaszok.get(str(szopar.id), '')
        helyes = adott_valasz.strip().lower() == szopar.angol.lower()
        eredmenyek.append({
            'magyar': szopar.magyar,
            'adott_valasz': adott_valasz,
            'helyes_valasz': szopar.angol,
            'helyes': helyes
        })
    # Tisztítsuk meg a session-t
    del request.session['kerdesek']
    del request.session['valaszok']
    return render(request, 'results.html', {'eredmenyek': eredmenyek})
