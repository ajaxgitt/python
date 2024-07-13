# If-else:
# Ejercicio:
# Escribe un programa en Python que solicite al usuario ingresar su edad. Luego, 
# determina si la persona es mayor de edad (18 años o más) y muestra un mensaje adecuado en función de la edad ingresada.



# def verificar_edad(edad):
#     if edad >= 18:
#         print('Used es mayor de edad..!')
#     else:
#         print('Usted es menor de edad..!')
        
# verificar_edad(14)
        




# For loop:
# Ejercicio:
# Escribe un programa en Python que imprima los primeros 5 números naturales (del 1 al 5) usando un bucle for.


# for i in range(2,6,2):
#     print(i)
    





# While loop:
# Ejercicio:
# Escribe un programa en Python que solicite al usuario ingresar un número entero positivo. Luego, 
# utiliza un bucle while para contar desde 1 hasta el número ingresado por el usuario.





# numero = int(input('Digite un numero: '))

# contador = 0


# while numero != contador:
#     contador += 1
#     print(contador)
    






# List comprehension:
# Ejercicio:
# Escribe un programa en Python que cree una lista con los cuadrados de los primeros 5 
# números naturales (del 1 al 5) utilizando list comprehension.


w =  [x*x for x in range(1,6) ]

print(w)





# Funciones:
# Ejercicio:
# Escribe una función en Python llamada es_primo que reciba un número entero positivo como argumento 
# y devuelva True si el número es primo, y False en caso contrario. Puedes usar un bucle for para 
# verificar si el número tiene divisores diferentes de 1 y sí mismo.

#import math

def es_esprimo(n):
    if n <=1: return False
    for i in range(2,int(n*0.5)+1):
        if n % i ==0: return False
    return True

print(es_esprimo(1))

r = lambda x:x <=1 == False
print(r)


