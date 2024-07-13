# Define una lista de números y usa map() para obtener una lista donde cada número se multiplique por 2.

lista_numeros = [1,5,8,9,68,7,65,2,63,5]

q = list(map(lambda x:x*2,lista_numeros))
#print(q)

# Crea una lista de palabras y convierte cada palabra a mayúsculas usando map().
lista_palabras = ['maria', 'dayana','yecid', 'genesis']
w = list(map(str.upper, lista_palabras))
print(w)



# Toma una lista de números como strings y usa map() para convertir cada uno a un número entero.

lista_numeros_str = ['1','2','3','4','5']

r = list(map(lambda x:int(x), lista_numeros_str))
#print(r)



# Define una lista de temperaturas en Celsius y usa map() para convertirlas a 
# Fahrenheit usando la fórmula (C * 9/5) + 32.

Celsius = [16, 32,-19,5,100,45]

Fahrenheit = list(map(lambda x:(x*9/5)+32, Celsius))

#print(Fahrenheit)



# Escribe una función map() que tome una lista de cadenas numéricas y 
# devuelva una lista de los números como floats.

k = list(map(lambda x: float(x),lista_numeros_str))
#print(k)


# Crea una lista de listas de números y usa map() para obtener una 
# lista de sumas de cada lista interna.



lista_de_listas_de_numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

p = list(map(lambda x: sum(x), lista_de_listas_de_numeros))








# Define una lista de nombres y usa map() para agregar un 
# saludo delante de cada nombre (por ejemplo, convertir "Juan" en "Hola Juan").
#print(lista_palabras)
saludo = list(map(lambda x: 'Hola '+x , lista_palabras ))

#print(saludo)













# Toma una lista de strings y usa map() para contar la longitud de cada palabra.

contar = list(map(lambda x: len(x), lista_palabras))

#print(contar)











# Escribe una función map() que tome una lista de listas y devuelva una lista 
# de la suma de los elementos de cada lista interna.

contar_elementos = list(map(lambda x: len(x),lista_de_listas_de_numeros ))

print(contar_elementos)






# Define una lista de fechas como strings en formato "dd-mm-yyyy" y 
# usa map() para convertirlas al formato "yyyy-mm-dd".

fechas = [
    "01-01-2023",
    "15-02-2023",
    "28-03-2023",
    "10-04-2023",
    "25-05-2023"
]
converir = list(map(lambda x : x[6:]+x[2:5]+'-'+x[0:2], fechas ))

print(converir)



