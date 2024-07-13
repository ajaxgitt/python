# Problema 1: Ordenar los Intervalos
# Descripción: Dados n intervalos [l, r], ordena los intervalos por el extremo izquierdo l. Si dos intervalos tienen el mismo extremo izquierdo, ordénalos por el extremo derecho r.

# Entrada:

# La primera línea contiene un entero n (1 ≤ n ≤ 10^5), el número de intervalos.
# Las siguientes n líneas contienen dos enteros l y r (1 ≤ l ≤ r ≤ 10^9), los extremos de cada intervalo.
# Salida:

# Imprime los n intervalos ordenados según las reglas especificadas.
# Ejemplo:

# makefile
# Copiar código
# Entrada:
# 3
# 1 3
# 2 5
# 1 2

# Salida:
# 1 2
# 1 3
# 2 5
# Problema 2: Caminos Más Cortos en un Grafo
# Descripción: Dado un grafo dirigido ponderado, encuentra la distancia más corta desde un nodo origen s a todos los demás nodos.

# Entrada:

# La primera línea contiene dos enteros n y m (1 ≤ n, m ≤ 10^5), el número de nodos y aristas, respectivamente.
# La siguiente línea contiene un entero s (1 ≤ s ≤ n), el nodo de origen.
# Las siguientes m líneas contienen tres enteros u, v, y w (1 ≤ u, v ≤ n; 1 ≤ w ≤ 10^9), indicando una arista dirigida desde el nodo u al nodo v con peso w.
# Salida:

# Imprime n enteros, donde el i-ésimo entero es la distancia más corta desde s al nodo i. Si no hay camino desde s al nodo i, imprime -1 para ese nodo.
# Ejemplo:

# makefile
# Copiar código
# Entrada:
# 5 6
# 1
# 1 2 2
# 1 3 4
# 2 3 1
# 2 4 7
# 3 5 3
# 4 5 1

# Salida:
# 0 2 3 9 6
# Problema 3: Subconjuntos Suma Cero
# Descripción: Dado un arreglo de n enteros, encuentra el número de subconjuntos no vacíos cuya suma es cero.

# Entrada:

# La primera línea contiene un entero n (1 ≤ n ≤ 20).
# La segunda línea contiene n enteros a_i (-10^9 ≤ a_i ≤ 10^9).
# Salida:

# Imprime el número de subconjuntos no vacíos cuya suma es cero.
# Ejemplo:

# makefile
# Copiar código
# Entrada:
# 4
# 3 -1 -1 -1

# Salida:
# 3
# Problema 4: Distancia Mínima entre Puntos
# Descripción: Dados n puntos en un plano 2D, encuentra la distancia mínima entre dos puntos distintos.

# Entrada:

# La primera línea contiene un entero n (2 ≤ n ≤ 10^5).
# Las siguientes n líneas contienen dos enteros x e y (-10^9 ≤ x, y ≤ 10^9), las coordenadas de cada punto.
# Salida:

# Imprime la distancia mínima entre dos puntos distintos con precisión de seis decimales.
# Ejemplo:

# makefile
# Copiar código
# Entrada:
# 3
# 0 0
# 1 1
# 2 2

# Salida:
# 1.414214
# Problema 5: Longest Increasing Subsequence (LIS)
# Descripción: Dado un arreglo de n enteros, encuentra la longitud de la subsecuencia creciente más larga.

# Entrada:

# La primera línea contiene un entero n (1 ≤ n ≤ 10^5).
# La segunda línea contiene n enteros a_i (1 ≤ a_i ≤ 10^9).
# Salida:

# Imprime la longitud de la subsecuencia creciente más larga.
# Ejemplo:

# makefile
# Copiar código
# Entrada:
# 6
# 10 22 9 33 21 50

# Salida:
# 4
# Problema 6: Problema de los N-Reinas
# Descripción: Coloca n reinas en un tablero de ajedrez n x n de manera que ninguna reina pueda atacar a otra. Imprime todas las soluciones posibles.

# Entrada:

# La primera línea contiene un entero n (1 ≤ n ≤ 10).
# Salida:

# Para cada solución, imprime una matriz n x n con el carácter Q indicando una reina y . indicando una casilla vacía. Imprime una línea en blanco entre soluciones.
# Ejemplo:

# makefile
# Copiar código
# Entrada:
# 4

# Salida:
# ..Q.
# Q...
# ...Q
# .Q..

# .Q..
# ...Q
# Q...
# ..Q.
# Estos problemas cubren una variedad de temas y niveles d