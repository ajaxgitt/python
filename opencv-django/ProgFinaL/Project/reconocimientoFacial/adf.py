
# @tiene_modelo
# def subir_foto(request):
#     if request.method == 'POST':
#         albumFormulario = AlbumForm(data=request.POST, usuario=request.user)
#         if albumFormulario.is_valid():
#             albumFormulario.save()
#             return redirect(reverse('subir_foto') + '?ok')
#     else:
#         albumFormulario = AlbumForm(usuario=request.user)
        
#     nombreUsuario = request.user  
#     ruta_archivos = f'C:/Users/yecid/Desktop/opencv-django/ProgFinaL/Project/models/{nombreUsuario}/'
#     carpetas = os.listdir(ruta_archivos)
#     modelo_nombre = carpetas[-1] 

#     ruta_modelo = f'{ruta_archivos}/{modelo_nombre}' 

#     modelo = load_model(ruta_modelo)

#     # Arquitectura del modelo
#     prototxt = 'C:/Users/yecid/Desktop/opencv-django/ProgFinaL/Project/reconocimientoFacial/model/deploy.prototxt'
#     # Pesos del modelo
#     model = 'C:/Users/yecid/Desktop/opencv-django/ProgFinaL/Project/reconocimientoFacial/model/res10_300x300_ssd_iter_140000.caffemodel'
#     confidence_threshold = 0.979
#     net = cv2.dnn.readNetFromCaffe(prototxt, model)
    
#     if request.method == "POST":
#         album_id = request.POST.get("album")
#         imagenes = request.FILES.getlist("imagenes")

#         if not album_id or not imagenes:
#             return JsonResponse({"status": "error", "message": "Falta la imagen o el álbum"})
        
#         album = get_object_or_404(Album, pk=album_id)
        
#         for imagen in imagenes:
#             # Leer la imagen desde el archivo cargado
#             np_img = np.fromstring(imagen.read(), np.uint8)
#             frame = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
#             height, width, _ = frame.shape
#             frame_resized = cv2.resize(frame, (300, 300))
#             blob = cv2.dnn.blobFromImage(frame_resized, 1.0, (300, 300), (104, 117, 123))
#             net.setInput(blob)
#             detections = net.forward()
#             for detection in detections[0][0]:
#                 if detection[2] > 0.9:
#                     box = detection[3:7] * [width, height, width, height]
#                     x_start, y_start, x_end, y_end = map(int, box)
#                     resized_face = cv2.resize(frame[y_start:y_end, x_start:x_end], (64, 64))
#                     resized_face = np.expand_dims(resized_face, axis=0)
#                     result = modelo.predict(resized_face)
#                     label = np.argmax(result, axis=1)[0]
#                     if label == 0:
#                         print('conocido')
#                         Foto.objects.create(album=album, imagen=imagen)
                        
#         return JsonResponse({"status": "success", "message": "Fotos subidas y procesadas correctamente"})
    
    
    
#     albums = Album.objects.filter(usuario=request.user)
#     context = {
#         'albumFormulario':albumFormulario,
#         'albums': albums
#     }
    
    
#     return render(request, "application/subir_foto.html", context)