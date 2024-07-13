# Doblar cada elemento de una lista:
# Dada una lista de números, crea una nueva lista donde cada elemento sea el doble
# del elemento correspondiente en la lista original.


lista_numeros = [1, 2, 3, 6, 10, 20, 30]

l = [x*2 for x in lista_numeros]

# print(l)


# Filtrar números pares:
# Dada una lista de números, crea una nueva lista que contenga solo los números
# pares de la lista original.


pares = [x for x in lista_numeros if x % 2 == 0]
# print(pares)


# Convertir strings a sus longitudes:
# Dada una lista de strings, crea una nueva lista donde cada elemento sea la
# longitud del string correspondiente en la lista original.


lista_str = ['maria', 'dayana', 'genesis', 'ilsen', 'mer']

nueva_lis = [len(x) for x in lista_str]

# print(nueva_lis)


# Eliminar elementos vacíos:
# Dada una lista que contiene strings y/o valores None, crea una nueva lista que
# contenga solo los strings no vacíos de la lista original.


lista = ['maria', None, 'dayana', False, 'genesis', 'ilsen', 'mer', None, '']

a = [x for x in lista if isinstance(x, str) and x != '']


# print(a)


# Crear una lista de tuplas:
# Dadas dos listas A y B del mismo tamaño, crea una lista de tuplas donde cada
# tupla contenga un elemento de A y su correspondiente elemento de B.


a = [1, 2, 3, 4, 5]
b = ['rojo', 'amarillo', 'verde', 'azul', 'lila']

c = [(a[i], b[i])for i in range(len(a))]

# print(c)


# Filtrar elementos únicos:
# Dada una lista que puede contener elementos duplicados, crea una nueva lista que
# contenga solo los elementos únicos de la lista original.

lista_original = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10, 10]


asdf = set()
# for i in lista_original:
#     asdf.add(i)
    
# print(list(asdf))

lista_unicos = [ x for x in lista_original if x not in asdf and not  asdf.add(x)]

#print(lista_unicos)


# Generar números pares y su cuadrado:
# Crea una lista de tuplas donde cada tupla contenga un número par y su cuadrado,
# para todos los números pares del 1 al 10.


lis_pares = [ (x, x**2) for x in range(1,11) if x % 2 ==0 ]

#print(lis_pares)






# Eliminar vocales de una lista de strings:
# Dada una lista de strings, crea una nueva lista donde cada string esté sin vocales
# (mayúsculas y minúsculas).


cadena = ['mAria','dayana','genesis','silvia','ilsen']

vocales = 'aeiou'


n = [''.join([x for x in y if x not in vocales]) for y  in cadena ]

#print(n)


# Crear una matriz cuadrada:
# Dado un número n, crea una lista de listas que represente una matriz cuadrada n x n,
# inicializada con ceros.











# Filtrar números primos:
# Dada una lista de números, crea una nueva lista que contenga solo los números
# primos de la lista original.

import math

def es_primo(n):
    if n <=1: return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0: return False
    return True


lisa_primos = [x for x in lista_original if es_primo(x)==True]

print(lisa_primos)