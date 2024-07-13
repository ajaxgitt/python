from django.db import models
from Application.models import User
from Application.models import Album

def carga_personalizada(instancia, nombre_archivo):
    return f'rostros/{instancia.usuario}/{nombre_archivo}'


class Recolectar_datos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to=carga_personalizada)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.usuario.username
    

def carga_personalizada(instancia, nombre_archivo):
    return f'modelos/{instancia.usuario}/{nombre_archivo}'

class ModeloEntrenado(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    archivo_modelo = models.FileField(upload_to=carga_personalizada)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


    
class FotosDondeApareces(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def guardarEnAlbum(self, filename):
        return f'galeria/fotos_donde_aprece_{self.usuario.username}/{filename}'

    imagen = models.ImageField(upload_to=guardarEnAlbum)

    def __str__(self):
        return f'Fotos donde aparece {self.usuario.username}'
    
    def save(self, *args, **kwargs):
        # Verificar si el usuario tiene un álbum "Fotos donde apareces"
        album_usuario, created = Album.objects.get_or_create(
            usuario=self.usuario, nombre='Fotos donde apareces')
        self.album = album_usuario
        super().save(*args, **kwargs)