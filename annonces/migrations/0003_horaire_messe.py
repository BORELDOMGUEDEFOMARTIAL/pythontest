# Generated by Django 3.1.2 on 2023-03-08 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonces', '0002_annonce_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horaire_messe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='')),
            ],
        ),
    ]
