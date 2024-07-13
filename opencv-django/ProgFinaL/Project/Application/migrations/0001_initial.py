# Generated by Django 5.0.6 on 2024-05-27 06:50

import Application.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('imagen', models.ImageField(upload_to=Application.models.Foto.guardarFotoEn)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.album')),
            ],
        ),
    ]
