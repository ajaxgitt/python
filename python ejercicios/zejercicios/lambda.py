lista_palabras = ['Ana','angeles','maria', 'zendaya','dayana','yecid', 'genesis','mer', 'marianela']
lista_numeros_str = ['1','2','3','4','5']
personas = [
    ("Juan", 25),
    ("María", 30),
    ("Pedro", 22),
    ("Ana", 27)
]
numeros = [-15, -10, -5, 0, 5, 10, -25, 30,99,-2]

lista_de_listas = [
    [4, 5, 6],
    [10, 11, 12],
    [7, 8, 9],
    [1, 2, 3],
    [1, 1, 1],
    
]

# Escribe una función lambda que sume dos números y luego úsala para calcular la suma de 3 y 5.

def suma(x, y): return x + y

# print(suma(3,5))


# Define una lista de números y usa una función lambda junto con map() para obtener una
# lista de los cuadrados de esos números.

cuadrados = list(map(lambda x: x**2 ,numeros))
#print(cuadrados)






# Crea una función lambda que tome una cadena y devuelva la cadena en mayúsculas.


mayus = list(map(str.upper, lista_palabras))
#print(mayus)


# Utiliza una función lambda en conjunto con filter() para filtrar los números pares de
# una lista de números enteros.

pares = list(filter(lambda x: x%2==0, numeros))

#print(pares)


# Define una lista de nombres y ordena esta lista alfabéticamente usando una función
# lambda con sorted().

ordenar = sorted(lista_palabras, key= lambda x:x[0].lower())
#print(ordenar)


# Escribe una función lambda que tome un número y devuelva True si es mayor que 10, y
# False en caso contrario. Luego, úsala para filtrar una lista de números.


res = list(filter(lambda x : x > 10, numeros))
#print(res)




# Define una lista de tuplas, donde cada tupla contiene un nombre y una edad. Usa una
# función lambda con sorted() para ordenar la lista por edad de manera ascendente.

edadd = sorted(personas, key=lambda x:x[1])
#print(edadd)




# Crea una función lambda que tome dos argumentos y devuelva el producto de ambos. Luego,
# usa esta función para calcular el producto de dos números ingresados por el usuario.

# x = int(input('numero 1: '))
# y = int(input('numero 2: '))


# res = lambda x , y: x*y 
# print(res(x,y))




from functools import reduce

# Define una lista de palabras y usa una función lambda con reduce() de la biblioteca functools
# para concatenar todas las palabras en una sola cadena.

l = reduce(lambda x , y: x + y, lista_palabras)
#print(l)






# Escribe una función lambda que tome un número y devuelva una cadena indicando si es positivo,
# negativo o cero. Luego, usa esta función para etiquetar una lista de números.

numeros = [-15, -10, -5, 0, 5, 10, -25, 30,99,-2,0]

etiquetar = list(map(lambda x : 'positivo' if x > 0 else ('negativo' if x < 0 else 'cero'), numeros))
print(etiquetar)
