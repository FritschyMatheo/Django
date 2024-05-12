from django.db import models

# Create your models here.

class Equipage(models.Model):
    nom=models.CharField(max_length=100)
    nombateau=models.CharField(max_length=100)
    capitaine=models.CharField(max_length=100)
    premiereapparition=models.IntegerField(null = True, blank=True)
    def __str__(self):
        if self.premiereapparition is not None:
            chaine = f"{self.nom} dirigé par {self.capitaine} est apparu au chapitre {self.premiereapparition} et navigue avec {self.nombateau}."
        else:
            chaine = f"{self.nom} dirigé par {self.capitaine} et navigue avec {self.nombateau}."
        return chaine
    
    def dictionnaire(self):
        return {"nom": self.nom, "nombateau": self.nombateau, "capitaine": self.capitaine, "premiereapparition": self.premiereapparition}


class Membre(models.Model):
    nom=models.CharField(max_length=100)
    poste=models.CharField(max_length=100)
    prime=models.IntegerField(null = True, blank=True)
    fruit=models.CharField(max_length=100, null = True, blank=True)
    def __str__(self):
        if self.prime is not None and self.fruit is not None:
            chaine = f"{self.nom} est {self.poste} de l'équipage. Il a une prime de {self.prime} berrys et possède le pouvoir du fruit : {self.fruit}."
        elif self.prime is not None:
            chaine = f"{self.nom} est {self.poste} de l'équipage. Il a une prime de {self.prime} berrys."
        elif self.fruit is not None:
            chaine = f"{self.nom} est {self.poste} de l'équipage. Il possède le pouvoir du fruit : {self.fruit}."
        else:
            chaine = f"{self.nom} est {self.poste} de l'équipage."
        return chaine
    
    def dictionnaire(self):
        return {"nom": self.nom, "poste": self.poste, "prime": self.prime, "fruit": self.fruit}