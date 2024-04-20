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
            'premiereapparition' : _('Chapitre de première apparition'),
        }