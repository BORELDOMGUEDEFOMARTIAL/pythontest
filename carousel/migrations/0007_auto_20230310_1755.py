# Generated by Django 3.1.2 on 2023-03-10 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carousel', '0006_auto_20230310_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article_paroissiale',
            name='document_pdf',
            field=models.FileField(blank=True, max_length=254, null=True, upload_to='public'),
        ),
        migrations.AlterField(
            model_name='article_paroissiale',
            name='document_word',
            field=models.FileField(blank=True, max_length=254, null=True, upload_to='public'),
        ),
    ]
