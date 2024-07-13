from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('baseInicio/',views.baseInicio, name='baseInicio'),
    # path('homeInicio/',views.homeInicio, name='homeInicio'),
    # path('subir_foto/',views.subir_foto, name='subir_foto'),
    # path('galeria/', views.galeria, name='galeria'),
    # path('otro/', views.otro, name='otro'),
    # path('explorar/', views.explorar, name='explorar'),
    # path('favoritos/', views.favoritos, name='favoritos'),
    # path('album/', views.album, name='album'),
    # path('carpeta_privada/', views.carpeta_privada, name='carpeta_privada'),
    # path('configuraciones/', views.configuraciones, name='configuraciones'),
    # path('mi_perfil/<int:user_id>', views.mi_perfil, name='mi_perfil'),
    # path('verFotos/<int:album_id>/', views.verFotos, name='verFotos'),
]
