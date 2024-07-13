lista_num = [1,2,3,4,5,8,12,6,7,9]
lista_nombre = ['maria','angeles', 'dayana', 'silvia', 'mer', 'alejandra']

# Ejercicios para filter()
# Define una lista de números y usa filter() para obtener solo los números pares.




pares = list(filter(lambda x: x%2==0,lista_num))
#print(pares)




# Crea una lista de palabras y usa filter() para obtener solo las palabras que tengan más de 5 caracteres.

caracteres = list(filter(lambda x : len(x)>=5, lista_nombre))

#print(caracteres)



# Toma una lista de números y usa filter() para obtener solo los números mayores que 10.

q = list(filter(lambda x :x>5, lista_num))

#print(q)








# Define una lista de strings y usa filter() para obtener solo las strings que contengan la letra 'a'.

g = list(filter(lambda x: 'a'in x, lista_nombre))
#print(g)







# Escribe una función filter() que tome una lista de números y devuelva solo 
# los números que sean divisibles por 3.

ww = list(filter(lambda x : x%3 ==0 , lista_num))

#print(ww)




# Crea una lista de tuplas (nombre, edad) y usa filter() para obtener 
# solo las personas menores de 18 años.



datos = [
    ('dayana', 23),
    ('maria', 24),
    ('leo', 14),
    ('yecid', 25),
    ('mer', 21),
    ('genesis', 8),
]



menores = list(filter(lambda x: x[1] < 19, datos))


#print(menores)



# Define una lista de strings y usa filter() para obtener solo las strings que 
# no empiecen con la letra 'a'.

t = list(filter(lambda x: x[0]!='a', lista_nombre))

#print(t)





# Toma una lista de números y usa filter() para obtener solo los números negativos.
o = [0,6,-90,-9,-5]
lista_num.extend(o)


ññ = list(filter(lambda x: x <0 , lista_num))

#print(ññ)







# Escribe una función filter() que tome una lista de palabras y devuelva 
# solo las palabras que sean palíndromos (se leen igual de adelante hacia atrás).

palindromes = [
    'radar',
    'oso',
    'reconocer',
    'rotor'
]

lista_nombre.extend(palindromes)

def es_palidromo(cadena: str)-> str:
    return cadena.lower().replace(' ','')[::-1] == cadena.lower().replace(' ','')
    
k = list(filter(lambda x : x.lower().replace(' ','') == x.lower().replace(' ','')[::-1] , lista_nombre))

#print(k)



# Define una lista de listas de números y usa filter() para obtener solo las 
# listas que tengan más de 3 elementos.

x = [2358,8962,87,258,4563,32107,47891]
lista_num.extend(x)

b = list(filter(lambda x: len(str(x))>3, lista_num))

print(b)

