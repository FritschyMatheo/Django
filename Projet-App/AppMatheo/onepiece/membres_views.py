from django.shortcuts import render, HttpResponseRedirect
from .forms import MembreForm
from . import models

def ajout(request, id):
    """if request.method == "POST":
        form = MembreForm(request)
        return HttpResponseRedirect("/onepiece/membres")
    else:"""
    form = MembreForm()
    return render(request,"onepiece/membres/creationmembre.html",{"form":form, "id": id})

def traitement(request, id):
    equipage = models.Equipage.objects.get(pk = id)
    lform = MembreForm(request.POST)
    if lform.is_valid():
        membre = lform.save(commit=False)
        membre.equipage = equipage
        membre.equipage_id = id
        membre.save()
        return render(request, "onepiece/membres/traitementmembre.html", {"membre" : membre})
    else:
        return render(request, "onepiece/membres/creationmembre.html", {"form" : lform})

def voirmembres(request):
    liste = list(models.Membre.objects.all())
    return render(request,"onepiece/membres/listemembres.html", {"liste" : liste})

def affiche(request, id):
    membre = models.Membre.objects.get( pk = id)
    return render(request,"onepiece/membres/membre.html", {"membre" : membre})

def update(request, id):
    membre = models.Membre.objects.get( pk = id)
    form = MembreForm(membre.dictionnaire())
    return render(request, "onepiece/membres/creationmembre.html", {"form" : form, "id": id})

def traitementupdate(request, id):
    equipage = models.Equipage.objects.get(pk = id)
    lform = MembreForm(request.POST)
    if lform.is_valid():
        membre = lform.save(commit=False)
        membre.id = id
        membre.equipage = equipage
        membre.equipage_id = id
        membre.save()
        return HttpResponseRedirect("/onepiece/membres")
    else:
        return render(request, "onepiece/membres/creationmembre.html", {"form" : lform, "id": id})
    
def delete(request, id):
    membre = models.Membre.objects.get( pk = id)
    membre.delete()
    return HttpResponseRedirect("/onepiece/membres")