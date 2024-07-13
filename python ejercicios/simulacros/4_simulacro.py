# Problema 1: Algoritmos de Grafos - Caminos Más Cortos y Ciclos Negativos
# Nivel: Avanzado

# Descripción: Dado un grafo dirigido con n nodos y m aristas, encuentra el camino más corto desde un nodo fuente s a todos los demás nodos. Si existe un ciclo negativo, infórmalo.

# Entrada:

# La primera línea contiene dos enteros n y m (1 ≤ n ≤ 10^5, 1 ≤ m ≤ 2*10^5).
# Las siguientes m líneas contienen tres enteros u, v y w (1 ≤ u, v ≤ n, -10^9 ≤ w ≤ 10^9), indicando una arista dirigida desde u a v con peso w.
# La última línea contiene un entero s (1 ≤ s ≤ n), el nodo fuente.
# Salida:

# Imprime el camino más corto desde s a todos los demás nodos. Si existe un ciclo negativo, imprime "Ciclo negativo detectado".
# Ejemplo:

# makefile
# Copiar código
# Entrada:
# 5 6
# 1 2 3
# 1 3 8
# 2 3 2
# 3 4 1
# 4 2 -7
# 4 5 2
# 1

# Salida:
# 0 3 5 6 8
# Problema 2: Programación Dinámica - Subarreglo Máximo con Suma Dada
# Nivel: Muy Avanzado

# Descripción: Dado un arreglo de n enteros, encuentra el subarreglo más largo cuya suma es exactamente k.

# Entrada:

# La primera línea contiene dos enteros n y k (1 ≤ n ≤ 10^5, -10^9 ≤ k ≤ 10^9).
# La segunda línea contiene n enteros a_i (-10^9 ≤ a_i ≤ 10^9).
# Salida:

# Imprime la longitud del subarreglo más largo cuya suma es exactamente k. Si no existe tal subarreglo, imprime -1.
# Ejemplo:

# makefile
# Copiar código
# Entrada:
# 5 7
# 1 2 3 4 5

# Salida:
# 3
# Problema 3: Teoría de Números - Contar Divisores en un Rango
# Nivel: Extremadamente Avanzado

# Descripción: Dado un rango [L, R] y un entero k, cuenta cuántos números en el rango tienen exactamente k divisores.

# Entrada:

# La primera línea contiene tres enteros L, R y k (1 ≤ L ≤ R ≤ 10^12, 1 ≤ k ≤ 100).
# Salida:

# Imprime el número de enteros en el rango [L, R] que tienen exactamente k divisores.
# Ejemplo:

# makefile
# Copiar código
# Entrada:
# 1 10 4

# Salida:
# 2
# Problema 4: Algoritmos de Ordenación y Búsqueda - Mediana de Medianas
# Nivel: Muy Avanzado

# Descripción: Dado un arreglo de n enteros, encuentra la mediana utilizando el algoritmo de mediana de medianas.

# Entrada:

# La primera línea contiene un entero n (1 ≤ n ≤ 10^5).
# La segunda línea contiene n enteros a_i (-10^9 ≤ a_i ≤ 10^9).
# Salida:

# Imprime la mediana del arreglo.
# Ejemplo:

# makefile
# Copiar código
# Entrada:
# 7
# 3 6 2 8 7 5 1

# Salida:
# 5
# Problema 5: Cadenas y Procesamiento de Texto - Suffix Array y LCP
# Nivel: Extremadamente Avanzado

# Descripción: Dada una cadena s, construye el arreglo de sufijos y el arreglo de LCP (longest common prefix).

# Entrada:

# La primera línea contiene una cadena s (1 ≤ |s| ≤ 2*10^5).
# Salida:

# Imprime el arreglo de sufijos y el arreglo de LCP.
# Ejemplo:

# yaml
# Copiar código
# Entrada:
# banana

# Salida:
# Suffix Array: 5 3 1 0 4 2
# LCP Array: 1 3 0 0 2
# Problema 6: Geometría Computacional - Cierre Convexo 3D
# Nivel: Experto

# Descripción: Dado un conjunto de n puntos en un espacio 3D, encuentra el cierre convexo (convex hull) de esos puntos.

# Entrada:

# La primera línea contiene un entero n (4 ≤ n ≤ 10^4).
# Las siguientes n líneas contienen tres enteros x, y y z (-10^9 ≤ x, y, z ≤ 10^9), las coordenadas de cada punto.
# Salida:

# Imprime los puntos que forman el cierre convexo en orden.
# Ejemplo:

# makefile
# Copiar código
# Entrada:
# 5
# 0 0 0
# 1 0 0
# 0 1 0
# 0 0 1
# 1 1 1

# Salida:
# 0 0 0
# 1 0 0
# 0 1 0
# 0 0 1
# Problema 7: Teoría de Juegos - Grundy Numbers
# Nivel: Muy Avanzado

# Descripción: Dado un juego de Nim generalizado con n pilas y sus tamaños iniciales, determina el ganador si ambos jugadores juegan óptimamente.

# Entrada:

# La primera línea contiene un entero n (1 ≤ n ≤ 1000).
# La segunda línea contiene n enteros a_i (1 ≤ a_i ≤ 10^9), los tamaños de las pilas.
# Salida:

# Imprime "Primer jugador" si el primer jugador tiene una estrategia ganadora, de lo contrario, imprime "Segundo jugador".
# Ejemplo:

# makefile
# Copiar código
# Entrada:
# 3
# 1 4 5

# Salida:
# Primer jugador
# Problema 8: Optimización y Aproximación - Caminos en un Grafo con Restricciones
# Nivel: Experto

# Descripción: Dado un grafo dirigido con n nodos y m aristas, encuentra el camino más corto del nodo 1 al nodo n que no pase por más de k aristas.

# Entrada:

# La primera línea contiene tres enteros n, m y k (1 ≤ n ≤ 500, 1 ≤ m ≤ 10^4, 1 ≤ k ≤ n).
# Las siguientes m líneas contienen tres enteros u, v y w (1 ≤ u, v ≤ n, 1 ≤ w ≤ 10^9), indicando una arista dirigida desde u a v con peso w.
# Salida:

# Imprime el peso del camino más corto que no pase por más de k aristas. Si no existe tal camino, imprime -1.
# Ejemplo:

# makefile
# Copiar código
# Entrada:
# 4 5 2
# 1 2 10
# 1 3 20
# 2 3 5
# 3 4 10
# 2 4 30

# Salida:
# 25
# Problema 9: Algoritmos Probabilísticos y Randomizados - Hashing de Cadenas
# Nivel: Avanzado

# Descripción: Dada una cadena s y q consultas, cada consulta pide verificar si dos substrings son iguales utilizando hashing.

# Entrada:

# La primera línea contiene una cadena s (1 ≤ |s| ≤ 10^5).
# La segunda línea contiene un entero q (1 ≤ q ≤ 10^5).
# Cada una de las siguientes q líneas contiene cuatro enteros l1, r1, l2 y r2 (1 ≤ l1, r1, l2, r2 ≤ |s|), representando dos substrings de s.
# Salida:

# Para cada consulta, imprime "Yes" si los substrings son iguales, de lo contrario imprime "No".
# Ejemplo:

# yaml
# Copiar código
# Entrada:
# abacaba
# 3
# 1 3 4 6
# 1 3 5 7
# 2 4 3 5

# Salida:
# Yes
# No
# Yes



