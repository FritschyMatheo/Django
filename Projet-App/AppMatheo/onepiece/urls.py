from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('ajoutequipage/', views.ajoutequipage),
    path('traitementequipage/', views.traitementEquipage),
    path('equipages/', views.voirequipages),
    path('equipage/<int:id>/', views.afficheequipage),
    path('update/<int:id>/', views.update),
    path('traitementupdate/<int:id>/', views.traitementupdate),
]