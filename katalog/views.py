from django.http import JsonResponse
from .models import Gra
from django.shortcuts import render

def index(request):
    return render(request, 'katalog/index.html')

def api_gry(request):
    dostepna_param = request.GET.get('dostepna')

    gry = Gra.objects.all()
    if dostepna_param == 'true':
        gry = gry.filter(dostepna=True)
    elif dostepna_param == 'false':
        gry = gry.filter(dostepna=False)

    data = []
    for g in gry:
        data.append({
            "id": g.id,
            "tytul": g.tytul,
            "gatunek": g.gatunek,
            "ocena": g.ocena,
            "dostepna": g.dostepna
        })
    return JsonResponse({"items": data})