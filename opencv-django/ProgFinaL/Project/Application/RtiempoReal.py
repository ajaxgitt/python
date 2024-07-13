import cv2
import numpy as np
from keras.models import load_model #type: ignore
from skimage.transform import resize
import os



def rFacialModelo(usuario):
        # Cargar el modelo entrenado
    user_folder = f'C:/Users/yecid/Desktop/opencv-django/ProgFinaL/Project/models/{usuario}/'
    
    # Obtén la lista de archivos en la carpeta del usuario
    files = [f for f in os.listdir(user_folder) if os.path.isfile(os.path.join(user_folder, f))]
    
    # Si no hay archivos en la carpeta, retorna None
    if not files:
        return None
    
    # Obtén la ruta completa de cada archivo
    files_paths = [os.path.join(user_folder, f) for f in files]
    
    # Selecciona el archivo más reciente basado en la fecha de modificación
    latest_file = max(files_paths, key=os.path.getmtime)
    
    
    modelo = load_model(latest_file)

    # Cargar el clasificador de rostros
    
    face_clsfr = cv2.CascadeClassifier('C:/Users/yecid/Desktop/opencv-django/ProgFinaL/Project/reconocimientoFacial/model/haarcascade_frontalface_default.xml')

    # Etiquetas y colores para las clases
    labels_dict = {0: usuario, 1: 'Desconocido'}
    color_dict = {0: (0, 255, 0), 1: (0, 0, 255)}
    try:
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        if not cap.isOpened():
            print("Error: No se puede abrir la cámara.")
            return
        while True:
            ret, frame = cap.read()

            if not ret:
                print('Error: No se pudo recibir el fotograma de la cámara.')
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_clsfr.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                face_img = frame[y:y+h, x:x+w]  # Recortar la imagen del rostro
                resized = resize(face_img, (64, 64, 3))  # Redimensionar la imagen a 64x64x3
                resized = np.expand_dims(resized, axis=0)  # Añadir una dimensión para el batch

                result = modelo.predict(resized)
                label = np.argmax(result, axis=1)[0]

                cv2.putText(frame, '{}'.format(labels_dict[label]), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color_dict[label], 2, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x+w, y+h), color_dict[label], 1)

            ret, jpeg = cv2.imencode('.jpg', frame)
            if not ret:
                print("Error: No se pudo codificar el fotograma.")
                break
            yield (b'--frame\r\n' + b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
    except Exception as e:
        print(f"Ocurrió un error: {e}")

    finally:
        if 'cap' in locals() and cap.isOpened():
            cap.release()
        yield (b'--frame\r\n' + b'Content-Type: text/plain\r\n\r\n' + b'END_OF_STREAM\r\n')

# Ejecutar la función de reconocimiento facial
# for frame in rFacialModelo():
#     print(frame)  # Aquí puedes enviar los frames al navegador o cualquier otra salida
