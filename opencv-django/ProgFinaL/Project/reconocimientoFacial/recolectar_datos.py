import cv2
from .models import Recolectar_datos
from django.core.files.base import ContentFile
import os

prototxt = "reconocimientoFacial/model/deploy.prototxt"
model = "reconocimientoFacial/model/res10_300x300_ssd_iter_140000.caffemodel"

def generar_imagenes(request):
    nombre_usuario = request.user.username
    net = cv2.dnn.readNetFromCaffe(prototxt, model)
    dataPath = 'C:/Users/yecid/Desktop/opencv-django/ProgFinaL/Project/media/rostros/' #Cambia a la ruta donde hayas almacenado Data
    personPath = dataPath + '/' + nombre_usuario

    if not os.path.exists(personPath):
        print('Carpeta creada: ',personPath)
        os.makedirs(personPath)
    try:
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        if not cap.isOpened():
            print("Error: No se puede abrir la cámara.")
            return

        count = 0
        while True:
            ret, frame = cap.read()

            if not ret:
                print('Error: No se pudo recibir el fotograma de la cámara.')
                break

            height, width, _ = frame.shape
            frame_resized = cv2.resize(frame, (300, 300))
            auxFrame = frame.copy()
            blob = cv2.dnn.blobFromImage(frame_resized, 1.0, (300, 300), (104, 117, 123))
            net.setInput(blob)
            detections = net.forward()

            for detection in detections[0][0]:
                if detection[2] > 0.99:
                    box = detection[3:7] * [width, height, width, height]
                    x_start, y_start, x_end, y_end = map(int, box)

                    cv2.rectangle(frame, (x_start, y_start), (x_end, y_end), (0, 255, 0), 1)
                    cv2.putText(frame, "Probabilidad: {:.2f}%".format(detection[2] * 100), (x_start, y_start - 15), 1, 1.2, (0, 255, 255), 1)

                    porcentaje = (count / 384) * 100
                    cv2.putText(frame, f'Recolectando datos... {round(porcentaje, 2)}%', (x_start, y_start - 30), 1, 1.2, (255, 106, 0), 1)

                    rostro = auxFrame[y_start:y_end, x_start:x_end]
                    rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
                    cv2.imwrite(personPath + '/rostro_{}.jpg'.format(count),rostro)
                    # rostro_objeto = Recolectar_datos(usuario=nombre_usuario)
                    # rostro_objeto.imagen.save('rostro_{}.jpg'.format(count), ContentFile(cv2.imencode('.jpg', rostro)[1].tobytes()))
                    # rostro_objeto.save()
                    
                    count += 1
                    print(count)

            ret, jpeg = cv2.imencode('.jpg', frame)
            if not ret:
                print("Error: No se pudo codificar el fotograma.")
                break
            yield (b'--frame\r\n' + b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

            if count >= 384:
                print('Se alcanzaron los 384 fotogramas.')
                break

    except Exception as e:
        print(f"Ocurrió un error: {e}")

    finally:
        if 'cap' in locals() and cap.isOpened():
            cap.release()
        yield (b'--frame\r\n' + b'Content-Type: text/plain\r\n\r\n' + b'END_OF_STREAM\r\n')
