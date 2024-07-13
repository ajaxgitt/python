from django.db import models
from user.models import User
import os




class Album(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'nombre: {self.nombre}, usuario: {self.usuario}'
    


class Foto(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, blank=True)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    faborito = models.BooleanField(default=False)
    
    
    def guardarFotoEn(self, filename):
        return f'galeria/{self.album.usuario}/{self.album.nombre}/{filename}'

    imagen = models.ImageField(upload_to=guardarFotoEn)

    def __str__(self):
        return f'albun: {self.album.nombre}, usuario: {self.album.usuario.username}'

    def save(self, *args, **kwargs):
        if not self.titulo:
            filename = os.path.basename(self.imagen.name)
            self.titulo = os.path.splitext(filename)[0]
        super(Foto, self).save(*args, **kwargs)
        
