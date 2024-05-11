from django.shortcuts import render, HttpResponseRedirect
from .forms import EquipageForm
from . import models


# Create your views here.

def index(request):
    return render(request, 'onepiece/index.html')

def ajoutequipage(request):
    if request.method == "POST":
        form = EquipageForm(request)

        """if form.is_valid():
            Equipage = form.save()"""
        return HttpResponseRedirect("/onepiece")
        #return render(request,"onepiece/equipage.html",{"form" : form})
    
        """else:
            return render(request,"onepiece/creationequipage.html",{"form":form})"""
    else:
        form = EquipageForm()
        return render(request,"onepiece/creationequipage.html",{"form":form})

def traitementEquipage(request):
    lform = EquipageForm(request.POST)
    if lform.is_valid():
        equipage = lform.save()
        return render(request, "onepiece/equipage.html", {"equipage" : equipage})
    else:
        return render(request, "onepiece/creationequipage.html", {"form" : lform})
    
def voirequipages(request):
    liste = list(models.Equipage.objects.all())
    return render(request,"onepiece/listeequipages.html", {"liste" : liste})