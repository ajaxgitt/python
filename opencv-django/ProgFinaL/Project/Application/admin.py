# admin.py

from django.contrib import admin
from .models import Album, Foto

class FotoInline(admin.TabularInline):
    model = Foto
    extra = 1  # Número de formularios vacíos adicionales para añadir fotos
    fields = ('imagen', 'titulo', 'faborito', 'fecha_creacion')  # Campos a mostrar en el inline
    readonly_fields = ('fecha_creacion',)  # Campos de solo lectura

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'usuario', 'fecha_creacion')
    list_filter = ('usuario', 'fecha_creacion')
    search_fields = ('nombre', 'usuario__username')
    inlines = [FotoInline]

admin.site.register(Album, AlbumAdmin)
admin.site.register(Foto)
