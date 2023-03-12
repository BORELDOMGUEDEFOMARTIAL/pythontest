from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *


app_name="galerie"
urlpatterns = [
   
     path('delete-galerie1<int:pk>',DeleteEglise_jacques_christophe.as_view(),name="delete-galerie1"),
     path('delete-galerie2<int:pk>',DeleteAccueil.as_view(),name="delete-galerie2"),
     path('delete-galerie3<int:pk>',DeleteSacre_coeur_gaumont.as_view(),name="delete-galerie3"),
     path('delete-galerie4<int:pk>',DeleteJeunes_18_35.as_view(),name="delete-galerie4"),
     path('delete-galerie5<int:pk>',DeleteSainte_anne.as_view(),name="delete-galerie5"),
     path('delete-galerie6<int:pk>',DeleteSainte_anne.as_view(),name="delete-galerie6"),
     path('add-galerie1', AddEglise_jacques_christophe.as_view() ,name="ajouter-galerie1"),
     path('add-galerie2', AddAccueil.as_view() ,name="ajouter-galerie2"),
     path('add-galerie3', AddSacre_coeur_gaumont.as_view() ,name="ajouter-galerie3"),
     path('add-galerie4', AddJeune_18_35.as_view() ,name="ajouter-galerie4"),
     path('add-galerie5', AddSainte_anne.as_view() ,name="ajouter-galerie5"),
     path('add-galerie6', AddLes_soeurs.as_view() ,name="ajouter-galerie6"),
    #  path('add-annonce', AddAnnonce.as_view() ,name="ajouter-annonce"),
]

