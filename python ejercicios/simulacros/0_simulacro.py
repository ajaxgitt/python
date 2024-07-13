

# Ejercicios más avanzados:

# Encontrar números primos hasta N:
# Escribe una función que encuentre todos los números primos menores o iguales a un número
# 𝑁
# N dado utilizando el algoritmo de la criba de Eratóstenes.


def algoritmo_de_Eratóstenes(n):
    lista_Eratóstenes = [True]*(n+1)
    lista_Eratóstenes[0] = lista_Eratóstenes[1] = False
    elemento = 2
    if lista_Eratóstenes[elemento] == True:
        for i in range(elemento * elemento, n+1, elemento):
            lista_Eratóstenes[i] = False
    elemento +=1
    lista_primos = []
    for i in range(n+1):
        if lista_Eratóstenes[i] == True:
            lista_primos.append(i)
    return lista_primos


n = 39
print(f"Los números primos hasta {n} son:")
print(algoritmo_de_Eratóstenes(n))


# Validar Sudoku:
# Escribe una función que tome una matriz 9x9 que representa un Sudoku y
# verifique si está resuelto correctamente.









# Encontrar el máximo subarray:
# Escribe una función que encuentre el subarray contiguo con la suma
# máxima en una lista de números enteros.









# Ordenar una lista de objetos:
# Escribe una función que tome una lista de objetos (por ejemplo,
# objetos con atributos como nombre, edad, etc.) y los ordene según un atributo específico.




# Implementar un algoritmo de búsqueda en grafos:
# Implementa un algoritmo de búsqueda en profundidad (DFS) o búsqueda
# en anchura (BFS) para buscar un elemento en un grafo representado como un diccionario de listas.








# Resolver el problema de las N reinas:
# Escribe una función que resuelva el problema de las N reinas para encontrar
# todas las posibles configuraciones de N reinas en un tablero de ajedrez NxN sin que se ataquen entre sí.


# Implementar un algoritmo de ordenación avanzado:
# Implementa un algoritmo de ordenación como QuickSort, MergeSort o HeapSort desde cero.


# Interpretar y ejecutar código Python dinámicamente:
# Escribe una función que tome una cadena de texto que representa código 
# Python y lo ejecute dinámicamente en tiempo de ejecución.


def codigo_python(codigo):
    try:
        exec(codigo)
    except Exception as e:
        print(f'Error nose pudo ejecutar el codigo {e}')
        





codigo_python("print('hola mundo!!!')")




# Crear un generador de contraseñas seguras:
# Escribe una función que genere contraseñas aleatorias seguras según ciertos criterios (longitud, caracteres especiales, etc.).

# Análisis de texto:
# Escribe una función que analice un texto grande y devuelva estadísticas como la frecuencia de palabras, la longitud promedio de las palabras, etc.



# Nivel Avanzado
# Ordenamiento por selección: Escribe una función que implemente el algoritmo de
# ordenamiento por selección.


# Buscar la subcadena más larga: Escribe una función que encuentre la
# subcadena más larga que se repite en una cadena dada.
