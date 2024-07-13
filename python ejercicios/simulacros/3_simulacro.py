# Problema 1: Caminos en un Grafo Dirigido Acíclico (DAG)
# Nivel: Avanzado

# Descripción: Dado un grafo dirigido acíclico (DAG) con n nodos y m aristas, encuentra el número de caminos distintos del nodo 1 al nodo n.

# Entrada:

# La primera línea contiene dos enteros n y m (1 ≤ n ≤ 10^5, 0 ≤ m ≤ 10^5).
# Las siguientes m líneas contienen dos enteros u y v (1 ≤ u, v ≤ n), indicando una arista dirigida desde u a v.
# Salida:

# Imprime el número de caminos distintos del nodo 1 al nodo n. Como el resultado puede ser muy grande, imprímelo módulo 10^9 + 7.
# Ejemplo:

# makefile
# Copiar código
# Entrada:
# 4 5
# 1 2
# 1 3
# 2 3
# 2 4
# 3 4

# Salida:
# 2
# Problema 2: Árboles de Segmento Dinámicos
# Nivel: Muy Avanzado

# Descripción: Implementa un árbol de segmento que soporte las siguientes operaciones:

# Update: Incrementa el valor en una posición específica.
# Query: Consulta la suma de un rango dado.
# Entrada:

# La primera línea contiene dos enteros n y q (1 ≤ n, q ≤ 10^5).
# La segunda línea contiene n enteros a_i (1 ≤ a_i ≤ 10^9).
# Las siguientes q líneas contienen una de las dos operaciones:
# 1 x v: Incrementa a[x] por v (1 ≤ x ≤ n, -10^9 ≤ v ≤ 10^9).
# 2 l r: Consulta la suma del rango [l, r] (1 ≤ l ≤ r ≤ n).
# Salida:

# Para cada operación de tipo 2, imprime la suma del rango [l, r].
# Ejemplo:

# makefile
# Copiar código
# Entrada:
# 5 5
# 1 2 3 4 5
# 2 1 3
# 1 2 10
# 2 1 3
# 1 4 -3
# 2 3 5

# Salida:
# 6
# 16
# 9
# Problema 3: Contar Subsecuencias Palindrómicas
# Nivel: Extremadamente Avanzado

# Descripción: Dada una cadena s, encuentra el número de subsecuencias palindrómicas distintas.

# Entrada:

# La primera línea contiene una cadena s (1 ≤ |s| ≤ 2*10^5).
# Salida:

# Imprime el número de subsecuencias palindrómicas distintas módulo 10^9 + 7.
# Ejemplo:

# makefile
# Copiar código
# Entrada:
# abcbaba

# Salida:
# 21
# Problema 4: K-Travelling Salesman Problem (K-TSP)
# Nivel: Extremadamente Avanzado

# Descripción: Dado un grafo completo con n nodos y m aristas y un entero k, encuentra el costo mínimo para que k vendedores ambulantes visiten todos los nodos exactamente una vez, comenzando y terminando en el nodo 1.

# Entrada:

# La primera línea contiene tres enteros n, m y k (2 ≤ n ≤ 18, 1 ≤ m ≤ n*(n-1)/2, 1 ≤ k ≤ n).
# Las siguientes m líneas contienen tres enteros u, v y w (1 ≤ u, v ≤ n, 1 ≤ w ≤ 10^9), indicando una arista no dirigida desde u a v con peso w.
# Salida:

# Imprime el costo mínimo para que k vendedores ambulantes visiten todos los nodos exactamente una vez, comenzando y terminando en el nodo 1.
# Ejemplo:

# makefile
# Copiar código
# Entrada:
# 4 6 2
# 1 2 10
# 1 3 15
# 1 4 20
# 2 3 35
# 2 4 25
# 3 4 30

# Salida:
# 80
# Problema 5: Estructuras Persistentes - Árbol de Segmento Persistente
# Nivel: Experto

# Descripción: Implementa un árbol de segmento persistente que soporte las siguientes operaciones:

# Update: Incrementa el valor en una posición específica en una versión dada.
# Query: Consulta la suma de un rango dado en una versión específica.
# Clone: Crea una nueva versión a partir de una versión existente.
# Entrada:

# La primera línea contiene dos enteros n y q (1 ≤ n, q ≤ 10^5).
# La segunda línea contiene n enteros a_i (1 ≤ a_i ≤ 10^9).
# Las siguientes q líneas contienen una de las tres operaciones:
# 1 v x v2: Incrementa a[x] por v2 en la versión v (1 ≤ x ≤ n, -10^9 ≤ v2 ≤ 10^9).
# 2 v l r: Consulta la suma del rango [l, r] en la versión v (1 ≤ l ≤ r ≤ n).
# 3 v: Crea una nueva versión a partir de la versión v.
# Salida:

# Para cada operación de tipo 2, imprime la suma del rango [l, r] en la versión especificada.
# Ejemplo:

# makefile
# Copiar código
# Entrada:
# 5 5
# 1 2 3 4 5
# 1 1 2 3
# 2 2 1 3
# 3 2
# 1 3 2 5
# 2 4 1 3

# Salida:
# 6
# 11
# Problema 6: Sistema de Partículas
# Nivel: Experto

# Descripción: Dado un conjunto de n partículas en el espacio 2D, cada partícula tiene una posición (x, y) y una velocidad (vx, vy). Encuentra el tiempo mínimo t para el cual la distancia máxima entre cualquier par de partículas sea mínima.

# Entrada:

# La primera línea contiene un entero n (2 ≤ n ≤ 1000).
# Las siguientes n líneas contienen cuatro enteros x, y, vx y vy (-10^9 ≤ x, y, vx, vy ≤ 10^9), representando la posición inicial y la velocidad de cada partícula.
# Salida:

# Imprime el tiempo mínimo t con una precisión de seis decimales.
# Ejemplo:

# makefile
# Copiar código
# Entrada:
# 3
# 0 0 1 1
# 0 1 1 0
# 1 0 0 1

# Salida:
# 0.500000
# Estos problemas están diseñados para ser e