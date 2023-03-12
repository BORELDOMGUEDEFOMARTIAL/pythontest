from django.db import models

# Create your models here.

class Eglise_jacques_christophe(models.Model):
    titre=models.CharField(max_length=150)
    # commentaire = models.TextField(default='NULL')
    date_publication= models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg')


    def __str__(self):
        return self.titre

class Sacre_coeur_bois_gaumont(models.Model):
    titre=models.CharField(max_length=150)
    # commentaire = models.TextField(default='NULL')
    date_publication= models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg')


    def __str__(self):
        return self.titre
class Jeune_18_35(models.Model):
    titre=models.CharField(max_length=150)
    # commentaire = models.TextField(default='NULL')
    date_publication= models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg')


    def __str__(self):
        return self.titre

class Les_soeurs(models.Model):
    titre=models.CharField(max_length=150)
    # commentaire = models.TextField(default='NULL')
    date_publication= models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg')


    def __str__(self):
        return self.titre
        
class Accueil(models.Model):
    titre=models.CharField(max_length=150)
    # commentaire = models.TextField(default='NULL')
    date_publication= models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg')


    def __str__(self):
        return self.titre
                         
                         
class Sainte_anne(models.Model):
    titre=models.CharField(max_length=150)
    # commentaire = models.TextField(default='NULL')
    date_publication= models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg')


    def __str__(self):
        return self.titre
                         
                         
                        
                         