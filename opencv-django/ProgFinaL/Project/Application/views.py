from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from user.models import User
from Application.utils import optener_datos_gogle
from .models import Album,Foto
from Application.forms import AlbumForm
from django.urls import reverse
from django.http import JsonResponse,HttpResponse
import os
import cv2
import numpy as np
from skimage.transform import resize
from keras.models import load_model #type: ignore
from reconocimientoFacial.models import FotosDondeApareces
from Application.reconocimientoF import rFacial
from Application.RtiempoReal import rFacialModelo
from django.http import StreamingHttpResponse
from Application.decorators import tiene_modelo





def home(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        return redirect('homeInicio',user_id=user_id)
    return render(request, 'application/home.html')

def Rfacial(request):
    return StreamingHttpResponse(rFacial(request), content_type='multipart/x-mixed-replace; boundary=frame')


def RfacialModelo(request):
    usuario = request.user.username
    return StreamingHttpResponse(rFacialModelo(usuario), content_type='multipart/x-mixed-replace; boundary=frame')

def demo(request):
    return render(request, 'application/demo.html')


def otro(request):
    fotos = FotosDondeApareces.objects.all()
    return render(request,'application/otro.html', {'fotos':fotos})



@tiene_modelo
def subir_foto(request):
    if request.method == 'POST':
        albumFormulario = AlbumForm(data=request.POST, usuario=request.user)
        if albumFormulario.is_valid():
            albumFormulario.save()
            return redirect(reverse('subir_foto') + '?ok')
    else:
        albumFormulario = AlbumForm(usuario=request.user)
        
    nombreUsuario = request.user  
    ruta_archivos = f'C:/Users/yecid/Desktop/opencv-django/ProgFinaL/Project/models/{nombreUsuario}/'
    carpetas = os.listdir(ruta_archivos)
    modelo_nombre = carpetas[-1] 

    ruta_modelo = f'{ruta_archivos}/{modelo_nombre}' 

    modelo = load_model(ruta_modelo)

    # Arquitectura del modelo
    prototxt = 'C:/Users/yecid/Desktop/opencv-django/ProgFinaL/Project/reconocimientoFacial/model/deploy.prototxt'
    # Pesos del modelo
    model = 'C:/Users/yecid/Desktop/opencv-django/ProgFinaL/Project/reconocimientoFacial/model/res10_300x300_ssd_iter_140000.caffemodel'
    confidence_threshold = 0.979
    net = cv2.dnn.readNetFromCaffe(prototxt, model)
    
    if request.method == "POST":
        album_id = request.POST.get("album")
        imagenes = request.FILES.getlist("imagenes")

        if not album_id or not imagenes:
            return JsonResponse({"status": "error", "message": "Falta la imagen o el álbum"})
        
        album = get_object_or_404(Album, pk=album_id)
        
        for imagen in imagenes:
            # Leer la imagen desde el archivo cargado
            np_img = np.fromstring(imagen.read(), np.uint8)
            frame = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
            height, width, _ = frame.shape
            frame_resized = cv2.resize(frame, (300, 300))
            blob = cv2.dnn.blobFromImage(frame_resized, 1.0, (300, 300), (104, 117, 123))
            net.setInput(blob)
            detections = net.forward()
            for detection in detections[0][0]:
                if detection[2] > 0.9:
                    box = detection[3:7] * [width, height, width, height]
                    x_start, y_start, x_end, y_end = map(int, box)
                    resized_face = cv2.resize(frame[y_start:y_end, x_start:x_end], (64, 64))
                    resized_face = np.expand_dims(resized_face, axis=0)
                    result = modelo.predict(resized_face)
                    label = np.argmax(result, axis=1)[0]
                    if label == 0:
                        print('conocido')
            Foto.objects.create(album=album, imagen=imagen)
                        
        return JsonResponse({"status": "success", "message": "Fotos subidas y procesadas correctamente"})
    
    
    
    albums = Album.objects.filter(usuario=request.user)
    context = {
        'albumFormulario':albumFormulario,
        'albums': albums
    }
    
    
    return render(request, "application/subir_foto.html", context)




@login_required
def baseInicio(request):
    if request.user.is_authenticated:
        foto_perfil = optener_datos_gogle(request.user)
    return render(request, 'application/baseInicio.html', {'foto_perfil': foto_perfil})



def homeInicio(request, user_id):
    mensaje = request.GET.get('mensaje', '')
    if request.user.is_authenticated:
        foto_perfil = optener_datos_gogle(request.user)
    usuario = get_object_or_404(User, id = user_id)
    if usuario.model:
        return redirect('Iniciomodel')
    else:
        return render(request, 'application/homeInicio.html', {'foto_perfil': foto_perfil,'mensaje':mensaje})
        
    
    
def Iniciomodel(request):
    if request.user.is_authenticated:
        foto_perfil = optener_datos_gogle(request.user)
    
    albumes = Album.objects.filter(usuario=request.user)[:3]
    fotos = Foto.objects.filter(album__usuario=request.user)
    
    context = {
        'albumes':albumes,
        'fotos':fotos,
        'foto_perfil':foto_perfil,
    }
    return render(request, 'application/Iniciomodel.html', context)


def galeria(request):
    
    if request.user.is_authenticated:
        foto_perfil = optener_datos_gogle(request.user)
    
    albumes = Album.objects.filter(usuario=request.user)[:3]
    fotos = Foto.objects.filter(album__usuario=request.user)
    
    context = {
        'albumes':albumes,
        'fotos':fotos,
        'foto_perfil':foto_perfil,
    }
    return render(request, 'application/galeria.html', context)
    
    
def verFotos(request, album_id):
    albumes = Album.objects.filter(usuario=request.user)[:3]
    fotos = Foto.objects.filter(album__usuario=request.user)
    
    try:
        album = Album.objects.get(id = album_id)
        foto = album.foto_set.all()
        context = {
        'albumes':albumes,
        'foto':foto,
        'fotos':fotos,
    }
        return render(request,'application/verfotos.html',context)
    except Album.DoesNotExist:
        return render(request,'application/home.html')
        
def explorar(request):
    if request.user.is_authenticated:
        foto_perfil = optener_datos_gogle(request.user)
    return render(request, 'application/explorar.html', {'foto_perfil': foto_perfil})
    



@tiene_modelo
def favoritos(request):
    if request.user.is_authenticated:
        foto_perfil = optener_datos_gogle(request.user)  # Asegúrate de tener definida esta función en tu proyecto
    
    fotos_favoritas = Foto.objects.filter(album__usuario=request.user, faborito=True)
    
    context = {
            'foto_perfil': foto_perfil,
            'fotos': fotos_favoritas,
        }
        
    return render(request, 'application/favoritos.html', context)


    


def album(request):
    if request.method == 'POST':
        albumFormulario = AlbumForm(data=request.POST, usuario=request.user)
        if albumFormulario.is_valid():
            albumFormulario.save()
            return redirect(reverse('album') + '?ok')
    else:
        albumFormulario = AlbumForm(usuario=request.user)
    foto_perfil = None
    if request.user.is_authenticated:
        foto_perfil = optener_datos_gogle(request.user)
        
    albumes = Album.objects.filter(usuario=request.user)
    fotos = Foto.objects.filter(album__usuario=request.user)
    
    dic = {}
    for foto in fotos:
        album_id = foto.album.id
        if album_id not in dic:
            dic[album_id] = {
                'imagen_url': foto.imagen.url,
                'album_nombre': foto.album.nombre,
                'album_descripcion': foto.album.descripcion,
            }

    context = {
        'albumes': albumes,
        'diccionario_fotos': dic,
        'foto_perfil': foto_perfil,
        'albumFormulario': albumFormulario,
    }

    return render(request, 'application/album.html', context)




def configuraciones(request):
        if request.user.is_authenticated:
            foto_perfil = optener_datos_gogle(request.user)
        return render(request, 'application/configuraciones.html', {'foto_perfil': foto_perfil})


def carpeta_privada(request):
        if request.user.is_authenticated:
            foto_perfil = optener_datos_gogle(request.user)
        return render(request, 'application/carpeta_privada.html', {'foto_perfil': foto_perfil})
    



@login_required
def mi_perfil(request, user_id):
    user = get_object_or_404(User, id = user_id)
    foto_perfil = None
    if request.user.is_authenticated:
        foto_perfil = optener_datos_gogle(request.user)
        return render(request, 'application/mi_perfil.html', {'foto_perfil': foto_perfil,'user':user})
    else:
        return render(request, 'application/mi_perfil.html',{'user':user})  






