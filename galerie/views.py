from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import AccueilForm,Sacre_coeur_bois_gaumontForm,Les_soeursForm,Jeunes_18_35Form,Sainte_anneForm,Eglise_jacques_christopheForm
from .models import Eglise_jacques_christophe,Sacre_coeur_bois_gaumont,Accueil,Les_soeurs,Jeune_18_35,Sainte_anne
# Create your views here.

class DeleteEglise_jacques_christophe(LoginRequiredMixin,DeleteView):
    model = Eglise_jacques_christophe
    success_url = "/galerie"
class DeleteAccueil(LoginRequiredMixin,DeleteView):
    model = Accueil
    success_url = "/galerie"
class DeleteLes_soeurs(LoginRequiredMixin,DeleteView):
    model = Les_soeurs
    success_url = "/galerie"
class DeleteJeunes_18_35(LoginRequiredMixin,DeleteView):
    model = Jeune_18_35
    success_url = "/galerie"
class DeleteSacre_coeur_gaumont(LoginRequiredMixin,DeleteView):
    model = Sacre_coeur_bois_gaumont
    success_url = "/galerie"
class DeleteSainte_anne(LoginRequiredMixin,DeleteView):
    model = Sainte_anne
    success_url = "/galerie"

class AddEglise_jacques_christophe(LoginRequiredMixin,CreateView):
    model= Eglise_jacques_christophe
    form_class = Eglise_jacques_christopheForm
    template_name="add-galerie1.html"
    success_url = "/galerie"
class AddAccueil(LoginRequiredMixin,CreateView):
    model= Accueil
    form_class = AccueilForm
    template_name="add-galerie2.html"
    success_url = "/galerie"
class AddSacre_coeur_gaumont(LoginRequiredMixin,CreateView):
    model= Sacre_coeur_bois_gaumont
    form_class = Sacre_coeur_bois_gaumontForm
    template_name="add-galerie3.html"
    success_url = "/galerie"
class AddJeune_18_35(LoginRequiredMixin,CreateView):
    model= Jeune_18_35
    form_class = Jeunes_18_35Form
    template_name="add-galerie4.html"
    success_url = "/galerie"
class AddSainte_anne(LoginRequiredMixin,CreateView):
    model= Sainte_anne
    form_class = Sainte_anneForm
    template_name="add-galerie5.html"
    success_url = "/galerie"
class AddLes_soeurs(LoginRequiredMixin,CreateView):
    model= Les_soeurs
    form_class = Les_soeursForm
    template_name="add-galerie6.html"
    success_url = "/galerie"
