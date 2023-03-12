# Generated by Django 3.1.2 on 2023-03-04 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galerie', '0005_auto_20230304_0144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sainte_anne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=150)),
                ('date_publication', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='accueil',
            name='commentaire',
        ),
        migrations.RemoveField(
            model_name='eglise_jacques_christophe',
            name='commentaire',
        ),
        migrations.RemoveField(
            model_name='jeune_18_35',
            name='commentaire',
        ),
        migrations.RemoveField(
            model_name='les_soeurs',
            name='commentaire',
        ),
        migrations.RemoveField(
            model_name='sacre_coeur_bois_gaumont',
            name='commentaire',
        ),
    ]