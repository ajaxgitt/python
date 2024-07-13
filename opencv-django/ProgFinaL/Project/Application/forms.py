from django import forms
from .models import Album, Foto
import os

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['nombre']
        
    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('usuario', None)
        super().__init__(*args, **kwargs)
        
    def save(self, commit=True):
        album = super().save(commit=False)
        if self.usuario:
            album.usuario = self.usuario
        if commit:
            album.save()
        return album
    

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['album', 'imagen']
    def save(self, commit=True):
        instance = super(FotoForm, self).save(commit=False)
        if not instance.titulo:
            filename = os.path.basename(self.cleaned_data['imagen'].name)
            instance.titulo = os.path.splitext(filename)[0]
        if commit:
            instance.save()
        return instance
