# Generated by Django 5.0.6 on 2024-06-11 20:07

import reconocimientoFacial.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reconocimientoFacial', '0009_fotosdondeapareces_album_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recolectar_datos',
            name='imagen',
            field=models.ImageField(upload_to=reconocimientoFacial.models.carga_personalizada),
        ),
    ]
