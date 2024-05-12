from django.urls import path
from . import views, membres_views

urlpatterns = [

    path('', views.index),

    # Partie équipages
    path('ajoutequipage/', views.ajoutequipage),
    path('traitementequipage/', views.traitementEquipage),
    path('equipages/', views.voirequipages),
    path('equipage/<int:id>/', views.afficheequipage),
    path('update/<int:id>/', views.update),
    path('traitementupdate/<int:id>/', views.traitementupdate),
    path('delete/<int:id>/', views.delete),

    # Partie membres
    path('ajoutmembre/', membres_views.ajoutmembre),
    path('traitementmembre/', membres_views.traitementmembre),
    path('membres/', membres_views.voirmembres),
    path('membre/<int:id>/', membres_views.affichemembre),
    path('updatemembre/<int:id>/', membres_views.update),
    path('traitementupdatemembre/<int:id>/', membres_views.traitementupdate),
    path('deletemembre/<int:id>/', membres_views.delete),
]