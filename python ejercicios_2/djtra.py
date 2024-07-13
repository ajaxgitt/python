import matplotlib.pyplot as plt
import osmnx as ox
from shapely.geometry import Polygon
import networkx as nx
import heapq


class Nodo:
    def __init__(self, id, atributos=None) -> None:
        self.id = id
        self.atributos = atributos if atributos is not None else {}

    def obtener_latitud(self):
        return self.atributos['y']

    def obtener_longitud(self):
        return self.atributos['x']

    def __repr__(self) -> str:
        return f'Nodo: ({self.id}, {self.atributos})'


class Enlace:
    def __init__(self, origen, destino, peso=1) -> None:
        self.origen = origen
        self.destino = destino
        self.peso = peso

    def __repr__(self) -> str:
        return f'Enlace origen:({self.origen.id} -> {self.destino.id},peso={self.peso}) '


class GrafoDirigido:

    def __init__(self) -> None:
        self.nodos = {}
        self.enlaces = []

    def _verificar_coordenadas(self, y, x):
        for id, nodo in self.nodos.items():
            if nodo.obtener_latitud() == y and nodo.obtener_longitud() == x:
                return id
        return None

    def buscar_ruta_mas_corta(self, origen_latitud, origen_longitud, destino_latitud, destino_longitud):
        id_origen = self._verificar_coordenadas(
            origen_latitud, origen_longitud)
        id_destino = self._verificar_coordenadas(
            destino_latitud, destino_longitud)

        if id_origen is not None and id_destino is not None and id_origen != id_destino:
            distancia, ruta = self.dijkstra(id_origen, id_destino)
            if distancia is not None:
                print(f'Distancia más corta: {distancia}')
                print(f'Ruta: {ruta}')
                self.dibujar_ruta(id_origen, id_destino, ruta)
            else:
                print('No se pudo encontrar una ruta válida.')
        else:
            if id_origen is None or id_destino is None:
                print('Error: Una o ambas coordenadas no corresponden a nodos válidos.')
            elif id_origen == id_destino:
                print('Error: Las coordenadas de origen y destino son iguales.')
            else:
                print('Error desconocido: No se pudo encontrar una ruta válida.')

    def dijkstra(self, origen_id, destino_id):
        # Inicialización
        distancias = {nodo_id: float('inf') for nodo_id in self.nodos}
        distancias[origen_id] = 0
        previo = {nodo_id: None for nodo_id in self.nodos}
        cola_prioridad = [(0, origen_id)]

        while cola_prioridad:
            distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

            if nodo_actual == destino_id:
                break

            for enlace in self.enlaces:
                if enlace.origen.id == nodo_actual:
                    distancia = distancia_actual + enlace.peso
                    if distancia < distancias[enlace.destino.id]:
                        distancias[enlace.destino.id] = distancia
                        previo[enlace.destino.id] = nodo_actual
                        heapq.heappush(
                            cola_prioridad, (distancia, enlace.destino.id))

        # Reconstrucción de la ruta más corta
        ruta = []
        nodo = destino_id
        while nodo is not None:
            ruta.append(nodo)
            nodo = previo[nodo]
        ruta.reverse()

        if distancias[destino_id] == float('inf'):
            return None, []
        return distancias[destino_id], ruta

    def obtener_numero_nodos(self):
        print(f'{len(self.nodos.keys())} nodos')
        return

    def obtener_numero_enlaces(self):
        print(f'{len(self.enlaces)} enlaces')
        return

    def agregar_nodo(self, nodo):
        if nodo.id not in self.nodos:
            self.nodos[nodo.id] = nodo
        else:
            print(f'El nodo con el id {nodo.id} ya existe en el grafo.!')

    def conectar_nodos(self, id_origen, id_destino, peso=1):
        if id_origen in self.nodos and id_destino in self.nodos:
            origen = self.nodos[id_origen]
            destino = self.nodos[id_destino]
            enlace = Enlace(origen, destino, peso)
            self.enlaces.append(enlace)
        else:
            print(f"Error: No se pueden conectar los nodos {id_origen} y {id_destino}. Al menos uno no existe.")

    def imprimir_enlaces(self):
        for i in self.enlaces:
            print(f'origen:{i.origen.id}-> destino {i.destino.id}')

    def imprimir_nodos(self):
        for _, valor in self.nodos.items():
            print(f'{valor}')

    def dibujar_grafo(self, coordenadas):
        polygon = Polygon(coordenadas)
        G_recortado = ox.graph_from_polygon(polygon, network_type='drive')
        ox.plot_graph(G_recortado,
                    figsize=(10, 10),
                    bgcolor='w',
                    node_color='lightblue',
                    node_size=30,
                    node_alpha=0.8,
                    edge_color='gray',
                    edge_linewidth=1.5,)
        plt.show()
        


    def dibujar_ruta(self, origen_id, destino_id, ruta):
        plt.figure(figsize=(10, 10))

        # Dibujar todos los nodos y enlaces
        for enlace in self.enlaces:
            plt.plot([self.nodos[enlace.origen.id].obtener_longitud(), self.nodos[enlace.destino.id].obtener_longitud()],
                    [self.nodos[enlace.origen.id].obtener_latitud(), self.nodos[enlace.destino.id].obtener_latitud()],color='gray', alpha=0.5)

        # Dibujar nodos
        for nodo_id, nodo in self.nodos.items():
            plt.scatter(nodo.obtener_longitud(), nodo.obtener_latitud(),
                        color='lightblue', s=100, zorder=2)
            plt.text(nodo.obtener_longitud(), nodo.obtener_latitud(),str(nodo.id), fontsize=12, ha='right')

        # Resaltar la ruta más corta
        for i in range(len(ruta) - 1):
            origen = self.nodos[ruta[i]]
            destino = self.nodos[ruta[i + 1]]
            plt.plot([origen.obtener_longitud(), destino.obtener_longitud()],
                    [origen.obtener_latitud(), destino.obtener_latitud()],
                    color='red', linewidth=2.5, zorder=1)

        plt.scatter(self.nodos[origen_id].obtener_longitud(
        ), self.nodos[origen_id].obtener_latitud(), color='green', s=200, zorder=3, label='Origen')
        plt.scatter(self.nodos[destino_id].obtener_longitud(
        ), self.nodos[destino_id].obtener_latitud(), color='blue', s=200, zorder=3, label='Destino')

        plt.legend()
        plt.show()


# Ejemplo de uso:
grafo = GrafoDirigido()

coordenadas = [
    (-63.181817, -17.766709),
    (-63.162407, -17.780224),
    (-63.172425, -17.799699),
    (-63.196322, -17.793340),
    (-63.197992, -17.778833)
]


polygon = Polygon(coordenadas)
G_recortado = ox.graph_from_polygon(polygon, network_type='drive')
nodos = G_recortado.nodes(data=True)
enlaces = list(G_recortado.edges(data=True))


for i in nodos:
    mi_nodo = Nodo(i[0], i[1])
    grafo.agregar_nodo(mi_nodo)

for i in enlaces:
    grafo.conectar_nodos(i[0], i[1], round(i[2]['length'], 2))


# Buscar ruta más corta y dibujar el grafo con la ruta
grafo.buscar_ruta_mas_corta(-17.7705527, -63.1789193, -17.7783472, -63.1652558)
