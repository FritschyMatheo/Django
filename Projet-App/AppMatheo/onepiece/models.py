from django.db import models

# Create your models here.

class Equipage(models.Model):
    nom=models.CharField(max_length=100)
    nombateau=models.CharField(max_length=100)
    capitaine=models.CharField(max_length=100)
    premiereapparition=models.IntegerField(blank=True)
    def __str__(self):
        if self.premiereapparition is not None:
            chaine = f"{self.nom} dirigé par {self.capitaine} est apparu au chapitre {self.premiereapparition} et navigue avec {self.nombateau}."
        else:
            chaine = f"{self.nom} dirigé par {self.capitaine} et navigue avec {self.nombateau}."
        return chaine