# Generated by Django 3.1.2 on 2023-03-04 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galerie', '0003_auto_20230303_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eglise_jacques_christophe',
            name='commentaire',
            field=models.TextField(default='NULL'),
        ),
    ]
