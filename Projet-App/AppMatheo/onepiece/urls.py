from django.urls import path
from . import views, membres_views

urlpatterns = [

    path('', views.index),

    # Partie équipages
    path('ajoutequipage/', views.ajout),
    path('traitementequipage/', views.traitement),
    path('equipages/', views.voirequipages),
    path('equipage/<int:id>/', views.affiche),
    path('update/<int:id>/', views.update),
    path('traitementupdate/<int:id>/', views.traitementupdate),
    path('delete/<int:id>/', views.delete),

    # Partie membres
    path('ajoutmembre/<int:id>/', membres_views.ajout),
    path('traitementmembre/<int:id>/', membres_views.traitement),
    path('membres/', membres_views.voirmembres),
    path('membre/<int:id>/', membres_views.affiche),
    path('updatemembre/<int:id>/', membres_views.update),
    path('traitementupdatemembre/<int:id>/', membres_views.traitementupdate),
    path('deletemembre/<int:id>/', membres_views.delete),
]