from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class EquipageForm(ModelForm):
    class Meta:
        model = models.Equipage
        fields = ('nom', 'nombateau', 'capitaine', 'premiereapparition')
        labels={
            'nom' : _('Nom'),
            'nombateau' : _('Nom du bateau'),
            'capitaine' : _('Capitaine de l\'équipage'),
            'premiereapparition' : _('Chapitre de première apparition')
        }

class MembreForm(ModelForm):
    class Meta:
        model = models.Membre
        fields = ('nom', 'poste', 'prime', 'fruit')
        labels={
            'nom' : _('Nom'),
            'poste' : _('Poste'),
            'prime' : _('Prime'),
            'fruit' : _('Fruit du démon'),
        }