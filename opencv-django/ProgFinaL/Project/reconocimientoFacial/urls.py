from django.urls import path
from .import views 

urlpatterns = [
    path('reconocimientoFacial/',views.reconocimientoFacial, name='reconocimientoFacial' ),
    path('recolectar-datos/', views.recolectarDatos, name='recolectarDatos'),
    path('entrenarModelo/<int:user_id>/',views.entrenarModelo, name='entrenarModelo'),
    path('buscandoSimilitudes/', views.buscandoSimilitudes, name='buscandoSimilitudes')
]