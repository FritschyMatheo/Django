from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('equipages/', views.equipages),
    path('ajoutequipage/', views.ajoutequipage),
    path('traitementequipage/', views.traitementEquipage),
    path('equipages/', views.voirequipages),
]