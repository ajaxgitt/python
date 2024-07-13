import cv2


prototxt = "reconocimientoFacial/model/deploy.prototxt"
model = "reconocimientoFacial/model/res10_300x300_ssd_iter_140000.caffemodel"

def rFacial(request):
    net = cv2.dnn.readNetFromCaffe(prototxt, model)
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

            height, width, _ = frame.shape
            frame_resized = cv2.resize(frame, (300, 300))
            blob = cv2.dnn.blobFromImage(frame_resized, 1.0, (300, 300), (104, 117, 123))
            net.setInput(blob)
            detections = net.forward()

            for detection in detections[0][0]:
                if detection[2] > 0.99:
                    box = detection[3:7] * [width, height, width, height]
                    x_start, y_start, x_end, y_end = map(int, box)

                    cv2.rectangle(frame, (x_start, y_start), (x_end, y_end), (0, 255, 0), 1)
                    cv2.putText(frame, "Rostro detectado: {:.2f}%".format(detection[2] * 100), (x_start, y_start - 15), 1, 1.2, (0, 255, 255), 1)

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
