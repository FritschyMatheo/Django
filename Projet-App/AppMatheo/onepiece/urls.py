from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('equipages/', views.equipages),
    path('ajoutequipage/', views.ajoutequipage),
    path('traitementequipage/', views.traitementEquipage),
]