# Dado un lista de strings, une todos los elementos usando join() para formar una sola cadena 
# separada por comas.


lista_strings = ['Hola', 'mundo', 'en', 'Python', '!', 'Estoy', 'aprendiendo', 'mucho']

unir = ', '.join(lista_strings)
#print(unir)




# Crea una función que reciba una lista de números como strings y devuelva una cadena 
# donde cada número esté separado por un espacio.

lisra_mun = ['1','2', '3','4','5']

def funcion(lista):
    cad = ' '.join(lista)
    return cad

#print(funcion(lisra_mun))


# Escribe un programa que solicite al usuario ingresar palabras separadas por espacios y luego 
# imprima esas palabras como una sola cadena separada por guiones bajos (_).

# palabras = input('digita palabras separadas por espacios: ')

# l = palabras.split()
# r = '_'.join(l)
#print(r)








# Dada una lista de nombres de frutas, utiliza join() para formar una oración que diga 
# "Me gusta comer: manzanas, naranjas, plátanos".



lista_frutas = ['manzanas','naranjas','plátanos','uvas'] 


w = f'Me gusta comer: {', '.join(lista_frutas)}'
#print(w)






# Crea una función que reciba una lista de números enteros y devuelva una cadena que 
# contenga todos los números como strings, separados por dos puntos (:).

lista_num = [1,2,3,4,5]


def numstr(lista):
    l = []
    for i in lista:
        l.append(str(i))
    r = ': '.join(l)
    return r

ww = [str(x) for x in lisra_mun]

res = ': '.join(ww)

#print(res)


#print(numstr(lista_num))






# Escribe un programa que tome una lista de palabras ingresadas por el usuario y las 
# imprima como una sola cadena, donde cada palabra esté separada por un punto y coma (;).


# q = input('escriba: ')

# rr = q.replace(',','').split()


# print('; '.join(rr))








# Dada una lista de nombres, usa join() para imprimir los nombres en una 
# sola línea separados por comas y un espacio.



lista_nombre = ['maria', 'dayana', 'silvia', 'mer']
#print(', '.join(lista_nombre))








# Crea una función que tome una lista de nombres y devuelva una cadena con los 
# nombres en mayúsculas, separados por un espacio.

def mayus(lista: list) -> str:
    return ' '.join([ i.upper() for i in lista ])


#print(mayus(lista_nombre))





# Escribe un programa que reciba una lista de números enteros y los convierta 
# en una cadena de dígitos separados por un guión (-).


f = '-'.join([ str(x) for x in lista_num ])

#print(f)






# Dada una lista de oraciones como strings, une todas las oraciones en un solo párrafo 
# separado por un salto de línea (\n).



lista_oraciones = [
    "Esta es la primera oración.",
    "Esta es la segunda oración.",
    "Y esta es la tercera oración."
]

print(lista_oraciones)
ñ = '\n'.join(lista_oraciones)
print(ñ)


