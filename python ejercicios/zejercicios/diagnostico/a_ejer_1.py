# Examen Diagnóstico de Python

# 1. Fundamentos de Python
# Pregunta 1: Escribe una función llamada es_primo que reciba un número entero y
# devuelva True si el número es primo y False en caso contrario.
import requests  # type: ignore
import random
import matplotlib.pyplot as plt
import math


def es_primo(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

# print(es_primo(59))


# Pregunta 2: Crea un generador llamado fibonacci que genere números de la serie de
# Fibonacci de forma indefinida.


def fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


g = fibo()
# print(next(g))
# print(next(g))


# 2. Estructuras de Datos
# Pregunta 3: Dado un diccionario con nombres de estudiantes como
# claves y sus calificaciones como valores, escribe una función llamada
# promedio_calificaciones que reciba el diccionario y devuelva el promedio
# de las calificaciones.

estudiantes = {
    'yecid': 70,
    'octavio': 100,
    'hexor': 78.5,
    'maria': 52
}


def promedio_calificaciones(estudiantes: dict) -> float:
    return sum(estudiantes.values())/len(estudiantes.keys())

# print(promedio_calificaciones(estudiantes))


# Pregunta 4: Implementa una clase Pila (stack) con los métodos apilar (push),
# desapilar (pop) y ver_cima (peek).


# 3. Programación Orientada a Objetos
# Pregunta 5: Define una clase llamada Círculo con un atributo radio.
# Incluye un método para calcular el área del círculo y otro para calcular el perímetro.

class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def areaCirculo(self):
        return round(math.pi*self.radio**2, 3)


circulito = Circulo(5)
# print(circulito.areaCirculo())


# Pregunta 6: Crea una clase Animal con un método hacer_sonido.
# Luego crea dos subclases, Perro y Gato, que hereden de Animal e
# implementen el método hacer_sonido con sonidos específicos
# ("guau" para perros y "miau" para gatos).


class Animal:
    def hacer_sonido(self):
        raise NotImplementedError('lorem')


class Gato(Animal):
    def hacer_sonido(self):
        return 'miau'


class Perro(Animal):
    def hacer_sonido(self):
        return 'guau'


pitbull = Perro()
angora = Gato()
# print(angora.hacer_sonido())
# print(pitbull.hacer_sonido())


# 4. Manejo de Archivos
# Pregunta 7: Escribe un programa que lea un archivo de texto línea por
# línea y cuente el número de palabras en el archivo.


with open('holi.txt', 'r')as archivo:
    contenido = archivo.read()


# print(len(contenido.split()))


# Pregunta 8: Crea una función que reciba una lista de diccionarios y escriba los datos en un archivo CSV.


# 5. Librerías y Módulos
# Pregunta 9: Utiliza la librería requests para hacer una solicitud HTTP GET a
# la API de GitHub para obtener información sobre un repositorio específico y muestra
# los datos en formato JSON.


propetario = 'ajaxgitt'
repo = 'nuevo'


url = f"https://api.github.com/repos/{propetario}/{repo}"

response = requests.get(url)

# if response.status_code == 200:
#     print(response.json())
# else:
#     print(f"Error: {response.status_code}")


# Pregunta 10: Usa la librería matplotlib para crear un gráfico de barras que muestre las
# ventas de un año, dado un diccionario con los meses como claves y las ventas como valores.


estadisticas = {
    'ENE': random.randint(1, 50000),
    'FEB': random.randint(1, 50000),
    'MAR': random.randint(1, 50000),
    'ABR': random.randint(1, 50000),
    'MAY': random.randint(1, 50000),
    'JUN': random.randint(1, 50000),
    'JUL': random.randint(1, 50000),
    'AGO': random.randint(1, 50000),
    'SEP': random.randint(1, 50000),
    'OCT': random.randint(1, 50000),
    'NOV': random.randint(1, 50000),
    'DIC': random.randint(1, 50000),
}

x = estadisticas.keys()
y = estadisticas.values()

colores = [
    'red', 'blue', 'green', 'purple', 'orange',
    'brown', 'pink', 'gray', 'olive', 'cyan',
    'magenta', 'yellow'
]

plt.bar(x, y, color=colores)

plt.title('Gráfico de Líneas desde Diccionario')
plt.xlabel('meses')
plt.ylabel('ventas')

# plt.show()


# 6. Concurrencia
# Pregunta 11: Escribe un programa que utilice threading para ejecutar dos funciones diferentes
# de manera concurrente. Una función debe contar de 1 a 10 con un retardo de 1 segundo entre
# cada número, y la otra debe contar de 10 a 1 con un retardo de 1 segundo entre cada número.


# import threading
# import time



# # Definir la primera función: contar de 1 a 10 con un retardo de 1 segundo entre cada número

# def contar_ascendete():
#     for i in range(1,11):
#         print(i)
#         time.sleep(1)

# # Definir la segunda función: contar de 10 a 1 con un retardo de 1 segundo entre cada número

# def contar_descendente():
#     for i in range(10,0,-1):
#         print(i)
#         time.sleep(1)


# inicio = time.perf_counter()
# # Crear los hilos

# hilo1= threading.Thread(target=contar_ascendete)
# hilo2= threading.Thread(target=contar_descendente)


# hilo1.start()
# hilo2.start()

# hilo1.join()
# hilo2.join()

# fin = time.perf_counter()

# tiempo = fin -inicio

# print(f'Se tardó {round(tiempo, 2)} segundos en ejecutar')


# 7. Expresiones Regulares
# Pregunta 12: Escribe una función que reciba una cadena de texto y use expresiones regulares
# para encontrar todas las direcciones de correo electrónico en la cadena.

import re


cad = r'^[a-zA-Z]+$'

f = re.search(cad,'yecidperez')

print(f)



















