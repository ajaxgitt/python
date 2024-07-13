# Ejercicios para reduce() (requiere importar desde functools)
# Importa reduce de functools y usa reduce() para obtener la suma de una lista de números.


from functools import reduce
lista_numeros = [1,5,8,9,68,7,65,2,63,5,100]
lista_palabras = ['maria', 'dayana','yecid', 'genesis','mer', 'marianela']
lista_numeros_str = ['1','2','3','4','5']

suma_num = reduce(lambda x,y:x+y,lista_numeros)

# print(suma_num)


# Define una lista de strings y usa reduce() para concatenar todas las strings en una sola cadena.

q = reduce(lambda x , y : x+y, lista_palabras)
# print(q)



# Toma una lista de números y usa reduce() para obtener el producto de todos los números.

w = reduce(lambda x , y : x *y , lista_numeros)
#print(w)



# Define una lista de diccionarios (con claves 'nombre' y 'edad') y usa reduce() para obtener la suma de todas las edades.


personas = [
    {'nombre': 'Juan', 'edad': 30},
    {'nombre': 'María', 'edad': 25},
    {'nombre': 'Pedro', 'edad': 35},
    {'nombre': 'Ana', 'edad': 28},
    {'nombre': 'Luis', 'edad': 32}
]



sum_edades = reduce(lambda x , y: x + y['edad'] ,personas, 0)

# print(sum_edades)




# Escribe una función reduce() que tome una lista de palabras y devuelva la palabra más larga.

w = reduce(lambda x, y : x if len(x) > len(y) else y , lista_palabras)
#print(w)






# Crea una lista de tuplas (nombre, salario) y usa reduce() para obtener la suma total de salarios.

empleados = [
    ('Juan', 3000),
    ('María', 3500),
    ('Pedro', 3200),
    ('Ana', 4000),
    ('Luis', 3800)
]



suma_salarios = reduce(lambda x ,y : x + y[1], empleados,0)

# print(suma_salarios)




# Define una lista de listas de números y usa reduce() para obtener una lista que contenga la suma 
# de los elementos de cada lista interna.

# Definir una lista de listas de números
lista_de_listas = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

sum_elementos = list(map(lambda lista: reduce(lambda x ,y : x+y,lista),lista_de_listas))

#print(sum_elementos)


# Toma una lista de números y usa reduce() con un lambda para obtener el máximo de la lista.

maximo = reduce(lambda x ,y : x if x > y else y , lista_numeros,0)




# Escribe una función reduce() que tome una lista de fechas como strings en formato 
# "yyyy-mm-dd" y devuelva la fecha más reciente.


fechas = [
    "2024-06-19",
    "2024-07-01",
    "2024-08-15",
    "2024-09-22",
    "2024-10-10"
]

mas_reciente = reduce(lambda x,y: x if x > y else y, fechas)

print(mas_reciente)











# Define una lista de listas de strings y usa reduce() para obtener una lista que contenga 
# la concatenación de todas las strings.


# Definir una lista de listas de strings
lista_de_listas = [
    ["manzana", "banana", "naranja"],
    ["perro", "gato", "pájaro"],
    ["rojo", "verde", "azul"]
]


unir = reduce(lambda x,y: x+y , lista_de_listas)
# print(unir)