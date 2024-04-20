from django.db import models

# Create your models here.

class Equipage(models.Model):
    nom=models.CharField(max_length=100)
    nombateau=models.CharField(max_length=100)
    capitaine=models.CharField(max_length=100)
    premiereapparition=models.IntegerField(blank=True)