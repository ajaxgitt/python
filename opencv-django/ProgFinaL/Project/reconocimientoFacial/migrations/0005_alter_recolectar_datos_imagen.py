# Generated by Django 5.0.6 on 2024-05-27 06:09

import reconocimientoFacial.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reconocimientoFacial', '0004_alter_recolectar_datos_imagen_modeloentrenado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recolectar_datos',
            name='imagen',
            field=models.ImageField(upload_to=reconocimientoFacial.models.carga_personalizada),
        ),
    ]
