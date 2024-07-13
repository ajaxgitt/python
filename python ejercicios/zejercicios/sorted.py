# Ejercicios para sorted()
lista_numeros = [1,5,8,9,68,7,65,2,63,5,100]
lista_palabras = ['maria', 'dayana','yecid', 'genesis','mer', 'marianela','zendaya']
lista_numeros_str = ['1','2','3','4','5']


# Define una lista de números y usa sorted() para ordenarla de menor a mayor.

w = sorted(lista_numeros, reverse=False)

# Crea una lista de palabras y usa sorted() para ordenarla alfabéticamente.

q = sorted(lista_palabras, reverse=True)
#print(q)

# Toma una lista de números y usa sorted() para ordenarla de mayor a menor.

ww = sorted(lista_numeros,reverse=True)
#print(ww)


# Define una lista de tuplas (nombre, edad) y usa sorted() para ordenarla por edad de manera ascendente.
personas = [
    ("Juan", 25),
    ("María", 30),
    ("Pedro", 22),
    ("Ana", 27)
]


ordenar_por_edad = sorted(personas, key=lambda x : x[1],reverse=False)

#print(ordenar_por_edad)


# Escribe una función sorted() que tome una lista de strings y devuelva las strings ordenadas por longitud (de menor a mayor).

ordd= sorted(lista_palabras,key=lambda x:len(x), reverse=True)
#print(ordd)




# Crea una lista de diccionarios (con claves 'nombre' y 'edad') y usa sorted() para ordenarla por nombre alfabéticamente.

personas = [
    {'nombre': 'Zendaya', 'edad': 32},
    {'nombre': 'Juan', 'edad': 30},
    {'nombre': 'María', 'edad': 25},
    {'nombre': 'yecid', 'edad': 32},
    {'nombre': 'Pedro', 'edad': 35},
    {'nombre': 'Ana', 'edad': 28},
    {'nombre': 'Luis', 'edad': 32}
]

abcd = sorted(personas, key=lambda x:x['nombre'].lower())
#print(abcd)


# Define una lista de números y usa sorted() con un lambda para ordenarla según el valor absoluto.

numeros = [-15, -10, -5, 0, 5, 10, 15, 20, -25, 30,-99,-2]



valor_absoluto = sorted(numeros, key= lambda x:abs(x))

#print(valor_absoluto)




# Toma una lista de strings y usa sorted() para ordenarla ignorando las mayúsculas/minúsculas (ordenar insensitivo al caso).

lista_palabras = ['angeles', 'maria', 'dayana','yecid', 'Alejandra','genesis','mer', 'marianela','zendaya']

ordenar_insensitivo =sorted(lista_palabras,key=lambda x:(x.lower(),x))
#print(ordenar_insensitivo)








# Escribe una función sorted() que tome una lista de fechas como strings en formato "dd-mm-yyyy" y las ordene cronológicamente.

fechas = [
    "19-06-2024",
    "01-07-2024",
    "10-12-2024",
    "15-08-2024",
    "22-09-2024",
    "10-10-2024",
    "15-01-2020",
]

f = sorted(fechas, key= lambda x : x[6:]+'-'+x[3:5]+'-'+x[:2])

# print(f)


# Define una lista de listas de números y usa sorted() para ordenarla según la suma de los elementos de 
# cada lista interna (de menor a mayor).


lista_de_listas = [
    [4, 5, 6],
    [10, 11, 12],
    [7, 8, 9],
    [1, 2, 3],
    [1, 1, 1],
    
]

sumaaa = sorted(lista_de_listas,key=lambda x:sum(x))
print(sumaaa)