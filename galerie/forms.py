from django.forms import ModelForm
from .models import Eglise_jacques_christophe,Accueil,Sacre_coeur_bois_gaumont,Sainte_anne,Jeune_18_35,Les_soeurs
from django import forms


class AccueilForm(forms.ModelForm):
    class Meta:
        model = Accueil
        fields = ['titre','image']
        widgets = {
            'titre':forms.TextInput(attrs={'class':'form-control'})
        }
class Eglise_jacques_christopheForm(forms.ModelForm):
    class Meta:
        model = Eglise_jacques_christophe
        fields = ['titre','image']
        widgets = {
            'titre':forms.TextInput(attrs={'class':'form-control'})
        }
class Sacre_coeur_bois_gaumontForm(forms.ModelForm):
    class Meta:
        model = Sacre_coeur_bois_gaumont
        fields = ['titre','image']
        widgets = {
            'titre':forms.TextInput(attrs={'class':'form-control'})
        }
class Sainte_anneForm(forms.ModelForm):
    class Meta:
        model = Sainte_anne
        fields = ['titre','image']
        widgets = {
            'titre':forms.TextInput(attrs={'class':'form-control'})
        }
class Les_soeursForm(forms.ModelForm):
    class Meta:
        model = Les_soeurs
        fields = ['titre','image']
        widgets = {
            'titre':forms.TextInput(attrs={'class':'form-control'})
        }
class Jeunes_18_35Form(forms.ModelForm):
    class Meta:
        model = Jeune_18_35
        fields = ['titre','image']
        widgets = {
            'titre':forms.TextInput(attrs={'class':'form-control'})
        }
