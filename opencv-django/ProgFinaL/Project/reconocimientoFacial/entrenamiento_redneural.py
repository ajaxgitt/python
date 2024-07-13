from keras.models import Sequential  # type: ignore
from keras.layers import Dense, Activation, Flatten, Dropout, Conv2D, MaxPooling2D # type: ignore
from keras.callbacks import ModelCheckpoint # type: ignore
from skimage.io import imread_collection
from skimage.transform import resize
import numpy as np
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical # type: ignore
import os
from user.models import User
from django.shortcuts import get_object_or_404
import logging

def crearModeloDNN(nombreUsuario, usuario_id):
    
    usuario = get_object_or_404(User, id = usuario_id )
    try:
        print('entrenando modelo...')
        datosUsuario = f'C:/Users/yecid/Desktop/opencv-django/ProgFinaL/Project/media/rostros/{nombreUsuario}/*.jpg'
        desconocido = f'C:/Users/yecid/Desktop/opencv-django/ProgFinaL/Project/reconocimientoFacial/data/desconocido/*.jpg'
        print(f'usuario: {len(datosUsuario)}')
        print(f'desconocido: {len(desconocido)}')
        # Load data
        imagesUsuario = imread_collection(datosUsuario)
        imagesDesconocido = imread_collection(desconocido)

        if len(imagesUsuario) == 0 or len(imagesDesconocido) == 0:
            raise ValueError("No se encontraron imágenes en una de las rutas especificadas.")

        # Combine data
        nUsuario = len(imagesUsuario)
        nDesconocido = len(imagesDesconocido)
        images = list(imagesUsuario) + list(imagesDesconocido)
        print("Total de imágenes: ", len(images))

        def Create_Y():
            return [0]*nUsuario + [1]*nDesconocido

        Y = Create_Y()
        Y = np.array(Y)

        # Resize images to a common size (64x64x3)
        X = []
        for img in images:
            if img.shape != (64, 64, 3):
                img = resize(img, (64, 64, 3), anti_aliasing=True)
            X.append(img)
        X = np.array(X)
        
        print(X[0].shape)

        # Model building
        modelo = Sequential()
        modelo.add(Conv2D(200, (3, 3), input_shape=X.shape[1:]))
        modelo.add(Activation('relu'))
        modelo.add(MaxPooling2D(pool_size=(2, 2)))

        modelo.add(Conv2D(100, (3, 3)))
        modelo.add(Activation('relu'))
        modelo.add(MaxPooling2D(pool_size=(2, 2)))

        modelo.add(Conv2D(50, (3, 3)))
        modelo.add(Activation('relu'))
        modelo.add(MaxPooling2D(pool_size=(2, 2)))

        modelo.add(Flatten())
        modelo.add(Dropout(0.5))
        modelo.add(Dense(50, activation='relu'))
        modelo.add(Dense(2, activation='softmax'))

        modelo.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        Y = to_categorical(Y)
        print(Y[0])
        print(Y[len(Y) - 1])

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.30, random_state=0)
        ruta = f'models/{nombreUsuario}'

        if not os.path.exists(ruta):
            os.makedirs(ruta)
        usuario.model = True
        usuario.save()
        checkpoint = ModelCheckpoint(ruta+'/model-{epoch:03d}.keras', monitor='val_loss', verbose=0, save_best_only=True, mode='auto')

        print('guardando!!')

        history = modelo.fit(X_train, Y_train, epochs=20, callbacks=[checkpoint], validation_split=0.2)

        print(history.history.keys())
        print(modelo.evaluate(X_test, Y_test))

        results = modelo.evaluate(X_test, Y_test)
        print(f"Test Loss: {results[0]}, Test Accuracy: {results[1]}")
        
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.error(f'Error al entrenar el modelo: {e}')
        raise

