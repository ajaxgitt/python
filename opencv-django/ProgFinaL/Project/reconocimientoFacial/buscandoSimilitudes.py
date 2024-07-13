import cv2
import numpy as np
from skimage.transform import resize
from keras.models import load_model
import os
from reconocimientoFacial.models import FotosDondeApareces

def buscando(nombreUsuario):
    
    ruta_archivos = f'C:/Users/yecid/Desktop/opencv-django/ProgFinaL/Project/models/{nombreUsuario}/'
    carpetas = os.listdir(ruta_archivos)
    modelo = carpetas[-1] 

    ruta_modelo = f'C:/Users/yecid/Desktop/opencv-django/ProgFinaL/Project/models/{nombreUsuario}/{modelo}' 

    modelo = load_model(ruta_modelo)

    # Arquitectura del modelo
    prototxt = "model/deploy.prototxt"
    # Pesos del modelo
    model = "model/res10_300x300_ssd_iter_140000.caffemodel"

    # Cargar el modelo redes neuronales profundas
    net = cv2.dnn.readNetFromCaffe(prototxt, model)

    album_imagenes = 'C:/Users/yecid/Desktop/opencv-django/ProgFinaL/Project/media/galeria/'
    imagenes = os.listdir(album_imagenes)

    for i in imagenes:
        rutaCompleta = os.path.join(album_imagenes, i)

        frame = cv2.imread(rutaCompleta)

        height, width, _ = frame.shape  # Obtiene las dimensiones del fotograma
        frame_resized = cv2.resize(frame, (300, 300))  # Redimensiona el fotograma a 300x300 píxeles
        auxFrame = frame.copy()

        # Crea un blob
        blob = cv2.dnn.blobFromImage(frame_resized, 1.0, (300, 300), (104, 117, 123))

        # ------- DETECCIONES Y PREDICCIONES ----------
        net.setInput(blob)  # Establece la entrada para el modelo
        detections = net.forward()  # Realiza la detección de objetos

        for detection in detections[0][0]:
            if detection[2] > 0.9:  # Si la confianza en la detección es mayor al 90%
                box = detection[3:7] * [width, height, width, height]  # Calcula las coordenadas del cuadro delimitador
                x_start, y_start, x_end, y_end = map(int, box)  # Convierte las coordenadas a enteros
                resized_face = resize(frame[y_start:y_end, x_start:x_end], (64, 64, 3))
                # Agregar una dimensión adicional para el lote de imágenes
                resized_face = np.expand_dims(resized_face, axis=0)
                result = modelo.predict(resized_face)
                label = np.argmax(result, axis=1)[0]
                label = np.argmax(result, axis=1)[0]
                if label == 0:
                    # Crea una instancia de FotosDondeApareces y guárdala en la base de datos
                    foto = FotosDondeApareces(usuario=nombreUsuario)
                    foto.imagen.save(i, frame)
                    

