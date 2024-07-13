# Problema 10: Árboles y Consultas en Línea - Árboles Dinámicos
# Nivel: Experto

# Descripción: Implementa un árbol dinámico que soporte las siguientes operaciones:

# Add Edge: Añade una arista a un árbol.
# Remove Edge: Elimina una arista de un árbol.
# Query: Consulta el nodo más cercano a un nodo dado u que esté en el mismo componente conectado.
# Entrada:

# La primera línea contiene dos enteros n y q (1 ≤ n, q ≤ 10^5).
# Las siguientes n-1 líneas contienen dos enteros u y v (1 ≤ u, v ≤ n, u ≠ v), indicando una arista del árbol.
# Las siguientes q líneas contienen una operación y sus parámetros:
# "1 u v": Añade una arista entre los nodos u y v.
# "2 u v": Elimina la arista entre los nodos u y v.
# "3 u": Consulta el nodo más cercano a u que está en el mismo componente conectado.
# Salida:

# Para cada operación de consulta "3 u", imprime el nodo más cercano en el mismo componente conectado que u.
# Ejemplo:

# makefile
# Copiar código
# Entrada:
# 5 5
# 1 2
# 2 3
# 3 4
# 4 5
# 3 1
# 1 2 4
# 3 1
# 2 1 2
# 3 1

# Salida:
# 2
# 2
# 1
# Problema 11: Algoritmos Probabilísticos y Randomizados - K-ésimo Elemento Más Pequeño
# Nivel: Avanzado

# Descripción: Dado un arreglo de n enteros, encuentra el k-ésimo elemento más pequeño utilizando un algoritmo probabilístico eficiente.

# Entrada:

# La primera línea contiene dos enteros n y k (1 ≤ n ≤ 10^5, 1 ≤ k ≤ n).
# La segunda línea contiene n enteros a_i (-10^9 ≤ a_i ≤ 10^9).
# Salida:

# Imprime el k-ésimo elemento más pequeño del arreglo.
# Ejemplo:

# makefile
# Copiar código
# Entrada:
# 5 3
# 5 2 9 1 7

# Salida:
# 5
# Problema 12: Árboles de Expansión Mínima - K-ésimo Árbol de Expansión Mínima
# Nivel: Experto

# Descripción: Dado un grafo no dirigido con n nodos y m aristas, encuentra el k-ésimo árbol de expansión mínima (Minimum Spanning Tree, MST).

# Entrada:

# La primera línea contiene dos enteros n y m (1 ≤ n ≤ 1000, 1 ≤ m ≤ 10^5).
# Las siguientes m líneas contienen tres enteros u, v y w (1 ≤ u, v ≤ n, 1 ≤ w ≤ 10^9), indicando una arista del grafo con peso w.
# La última línea contiene un entero k (1 ≤ k ≤ 1000), el índice del árbol de expansión mínima que se desea encontrar.
# Salida:

# Imprime el peso del k-ésimo MST. Si hay menos de k árboles de expansión mínima, imprime -1.
# Ejemplo:

# makefile
# Copiar código
# Entrada:
# 4 5
# 1 2 1
# 2 3 2
# 3 4 3
# 4 1 4
# 1 3 5
# 2
# 2

# Salida:
# 5
# Problema 13: Problema del Vendedor Viajero (TSP) - Heurística Constructiva
# Nivel: Muy Avanzado

# Descripción: Dado un conjunto de n ciudades y las distancias entre ellas, encuentra un ciclo hamiltoniano de longitud mínima utilizando una heurística constructiva como la inserción más barata (Cheapest Insertion).

# Entrada:

# La primera línea contiene un entero n (2 ≤ n ≤ 20), el número de ciudades.
# Las siguientes n líneas contienen n enteros, donde el entero en la i-ésima línea y j-ésima columna representa la distancia entre la ciudad i y la ciudad j.
# Salida:

# Imprime la longitud mínima del ciclo hamiltoniano encontrado.
# Ejemplo:

# makefile
# Copiar código
# Entrada:
# 4
# 0 1 2 3
# 1 0 4 5
# 2 4 0 6
# 3 5 6 0

# Salida:
# 10
# Problema 14: Problema de Asignación - Algoritmo Húngaro
# Nivel: Experto

# Descripción: Dada una matriz cuadrada de costos de asignación, encuentra la asignación óptima utilizando el algoritmo húngaro (Hungarian Algorithm).

# Entrada:

# La primera línea contiene un entero n (1 ≤ n ≤ 100), el tamaño de la matriz.
# Las siguientes n líneas contienen n enteros, donde el entero en la i-ésima línea y j-ésima columna representa el costo de asignar el trabajador i a la tarea j.
# Salida:

# Imprime el costo mínimo de la asignación óptima.
# Ejemplo:

# makefile
# Copiar código
# Entrada:
# 3
# 3 2 7
# 5 1 3
# 2 6 8

# Salida:
# 5
# Problema 15: Geometría Computacional - Problema de los Pares Más Cercanos
# Nivel: Muy Avanzado

# Descripción: Dado un conjunto de n puntos en el plano, encuentra la distancia mínima entre dos puntos utilizando el algoritmo de pares más cercanos.

# Entrada:

# La primera línea contiene un entero n (2 ≤ n ≤ 10^5), el número de puntos.
# Las siguientes n líneas contienen dos enteros x y y (-10^9 ≤ x, y ≤ 10^9), las coordenadas de cada punto.
# Salida:

# Imprime la distancia mínima entre dos puntos.
# Ejemplo:

# makefile
# Copiar código
# Entrada:
# 4
# 0 0
# 3 4
# 1 1
# -1 -1

# Salida:
# 1.41421356