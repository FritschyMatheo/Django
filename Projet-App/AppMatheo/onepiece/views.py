from django.shortcuts import render
from .forms import EquipageForm
from . import models


# Create your views here.

def index(request):
    return render(request, 'onepiece/index.html')

def equipages(request):
    return render(request, 'onepiece/equipages.html')

def ajoutequipage(request):
    if request.method == "POST":
        form = EquipageForm(request)
        if form.is_valid():
            Equipage = form.save()
            return render(request,"onepiece/equipages.html",{"Equipage : Equipage"})
        else:
            return render(request,"onepiece/creationequipage.html",{"form":form})
    else:
        form = EquipageForm()
        return render(request,"onepiece/creationequipage.html",{"form":form})

def traitementEquipage(request):
    lform = EquipageForm(request.POST)
    if lform.is_valid():
        Equipage = lform.save()
        return render(request, "onepiece/equipages.html", {"Equipage" : Equipage})
    else:
        return render(request, "onepiece/creationequipage.html", {"form" : lform})