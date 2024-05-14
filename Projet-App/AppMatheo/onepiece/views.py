from django.shortcuts import render, HttpResponseRedirect
from .forms import EquipageForm
from . import models


# Create your views here.

def index(request):
    return render(request, 'onepiece/index.html')

def ajout(request):
    if request.method == "POST":
        form = EquipageForm(request)

        """if form.is_valid():
            Equipage = form.save()"""
        return HttpResponseRedirect("/onepiece/equipages")
        #return render(request,"onepiece/equipage.html",{"form" : form})
    
        """else:
            return render(request,"onepiece/creationequipage.html",{"form":form})"""
    else:
        form = EquipageForm()
        return render(request,"onepiece/equipages/creationequipage.html",{"form":form})

def traitement(request):
    lform = EquipageForm(request.POST)
    if lform.is_valid():
        equipage = lform.save()
        return render(request, "onepiece/equipages/traitementequipage.html", {"equipage" : equipage})
    else:
        return render(request, "onepiece/equipages/creationequipage.html", {"form" : lform})
    
def voirequipages(request):
    liste = list(models.Equipage.objects.all())
    return render(request,"onepiece/equipages/listeequipages.html", {"liste" : liste})

def affiche(request, id):
    equipage = models.Equipage.objects.get( pk = id)
    return render(request,"onepiece/equipages/equipage.html", {"equipage" : equipage})

def update(request, id):
    equipage = models.Equipage.objects.get( pk = id)
    form = EquipageForm(equipage.dictionnaire())
    return render(request, "onepiece/equipages/creationequipage.html", {"form" : form, "id": id})

def traitementupdate(request, id):
    lform = EquipageForm(request.POST)
    if lform.is_valid():
        equipage = lform.save(commit=False)
        equipage.id = id
        equipage.save()
        return render(request, "onepiece/equipages/traitementequipage.html", {"equipage" : equipage})
    else:
        return render(request, "onepiece/equipages/creationequipage.html", {"form" : lform, "id": id})
    
def delete(request, id):
    equipage = models.Equipage.objects.get( pk = id)
    equipage.delete()
    return HttpResponseRedirect("/onepiece/equipages")