#  Grafos (Graphs)
# Conceptos básicos: Vertices y aristas, representaciones (listas de adyacencia, matrices de adyacencia).
# Algoritmos de recorrido: BFS (Breadth-First Search), DFS (Depth-First Search).
# Algoritmos avanzados: Dijkstra, Prim, Kruskal.



from collections import defaultdict, deque
import heapq

class Grafo:
    def __init__(self):
        self.lista_adyacencia = defaultdict(dict)
        self.matriz_adyacencia = []
        self.vertices = []
    
    def agregar_vertice(self, vertice):
        if vertice not in self.lista_adyacencia:
            self.lista_adyacencia[vertice] = {}
            self.vertices.append(vertice)
            for fila in self.matriz_adyacencia:
                fila.append(0)
            self.matriz_adyacencia.append([0] * len(self.vertices))
    
    def agregar_arista(self, desde_vertice, hacia_vertice, peso=1):
        if desde_vertice in self.lista_adyacencia and hacia_vertice in self.lista_adyacencia:
            self.lista_adyacencia[desde_vertice][hacia_vertice] = peso
            self.lista_adyacencia[hacia_vertice][desde_vertice] = peso  # Para grafos no dirigidos
            idx_desde = self.vertices.index(desde_vertice)
            idx_hacia = self.vertices.index(hacia_vertice)
            self.matriz_adyacencia[idx_desde][idx_hacia] = peso
            self.matriz_adyacencia[idx_hacia][idx_desde] = peso  # Para grafos no dirigidos
    
    # Recorrido BFS
    def bfs(self, vertice_inicial):
        visitados = set()
        cola = deque([vertice_inicial])
        resultado = []
        
        while cola:
            vertice = cola.popleft()
            if vertice not in visitados:
                visitados.add(vertice)
                resultado.append(vertice)
                for vecino in self.lista_adyacencia[vertice]:
                    if vecino not in visitados:
                        cola.append(vecino)
        
        return resultado
    
    # Recorrido DFS
    def dfs(self, vertice_inicial):
        visitados = set()
        pila = [vertice_inicial]
        resultado = []
        
        while pila:
            vertice = pila.pop()
            if vertice not in visitados:
                visitados.add(vertice)
                resultado.append(vertice)
                for vecino in self.lista_adyacencia[vertice]:
                    if vecino not in visitados:
                        pila.append(vecino)
        
        return resultado
    
    # Algoritmo de Dijkstra
    def dijkstra(self, vertice_inicial):
        distancias = {vertice: float('infinity') for vertice in self.lista_adyacencia}
        distancias[vertice_inicial] = 0
        cola_prioridad = [(0, vertice_inicial)]
        heapq.heapify(cola_prioridad)
        
        while cola_prioridad:
            distancia_actual, vertice_actual = heapq.heappop(cola_prioridad)
            if distancia_actual > distancias[vertice_actual]:
                continue
            for vecino, peso in self.lista_adyacencia[vertice_actual].items():
                distancia = distancia_actual + peso
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    heapq.heappush(cola_prioridad, (distancia, vecino))
        
        return distancias

    # Algoritmo de Prim
    def prim(self):
        if not self.vertices:
            return []
        
        mst = []
        visitados = set()
        aristas = [(0, self.vertices[0], self.vertices[0])]
        heapq.heapify(aristas)
        
        while aristas:
            peso, desde_vertice, hacia_vertice = heapq.heappop(aristas)
            if hacia_vertice not in visitados:
                visitados.add(hacia_vertice)
                mst.append((desde_vertice, hacia_vertice, peso))
                for vecino, peso in self.lista_adyacencia[hacia_vertice].items():
                    if vecino not in visitados:
                        heapq.heappush(aristas, (peso, hacia_vertice, vecino))
        
        return mst[1:]  # Eliminar el primer elemento que es un auto-bucle

    # Algoritmo de Kruskal
    def kruskal(self):
        def find(raices, vertice):
            if raices[vertice] != vertice:
                raices[vertice] = find(raices, raices[vertice])
            return raices[vertice]

        def union(raices, rangos, vertice1, vertice2):
            raiz1 = find(raices, vertice1)
            raiz2 = find(raices, vertice2)
            if raiz1 != raiz2:
                if rangos[raiz1] > rangos[raiz2]:
                    raices[raiz2] = raiz1
                else:
                    raices[raiz1] = raiz2
                    if rangos[raiz1] == rangos[raiz2]:
                        rangos[raiz2] += 1

        aristas = []
        for desde_vertice, vecinos in self.lista_adyacencia.items():
            for hacia_vertice, peso in vecinos.items():
                if (hacia_vertice, desde_vertice, peso) not in aristas:
                    aristas.append((desde_vertice, hacia_vertice, peso))
        
        aristas.sort(key=lambda x: x[2])
        raices = {vertice: vertice for vertice in self.vertices}
        rangos = {vertice: 0 for vertice in self.vertices}
        
        mst = []
        for desde_vertice, hacia_vertice, peso in aristas:
            if find(raices, desde_vertice) != find(raices, hacia_vertice):
                union(raices, rangos, desde_vertice, hacia_vertice)
                mst.append((desde_vertice, hacia_vertice, peso))
        
        return mst

# Ejemplo de uso:
g = Grafo()
g.agregar_vertice('A')
g.agregar_vertice('B')
g.agregar_vertice('C')
g.agregar_vertice('D')
g.agregar_arista('A', 'B', 1)
g.agregar_arista('B', 'C', 2)
g.agregar_arista('A', 'C', 4)
g.agregar_arista('C', 'D', 1)

print("Lista de adyacencia:")
# g.mostrar_lista_adyacencia()

print("\nMatriz de adyacencia:")
for fila in g.matriz_adyacencia:
    print(fila)

print("\nBFS desde 'A':")
print(g.bfs('A'))

print("\nDFS desde 'A':")
print(g.dfs('A'))

print("\nDijkstra desde 'A':")
print(g.dijkstra('A'))

print("\nMST usando Prim:")
print(g.prim())

print("\nMST usando Kruskal:")
print(g.kruskal())
