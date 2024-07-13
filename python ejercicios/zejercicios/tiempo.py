import timeit

# Función que quieres medir
def funcion_a():
    # Código de la función
    r = 1 + 1 
    return r

def funcion_b():
    # Código de la función
    return 1 + 1 

# Medir el tiempo de ejecución de funcion_a
tiempo_a = timeit.timeit("funcion_a()", globals=globals(), number=1000)

# Medir el tiempo de ejecución de funcion_b
tiempo_b = timeit.timeit("funcion_b()", globals=globals(), number=1000)

print(f"Tiempo de funcion_a: {tiempo_a} segundos")
print(f"Tiempo de funcion_b: {tiempo_b} segundos")
