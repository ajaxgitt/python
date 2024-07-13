

import matplotlib.pyplot as plt
import networkx as nx


class Nodo:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        
class Enlace:
    def __init__(self, nodo_origen, nodo_destino) -> None:
        self.nodo_origen = nodo_origen
        self.nodo_destino = nodo_destino
        
    def obtener_origen(self):
        return self.nodo_origen
    
    def obtener_destino(self):
        return self.nodo_destino

class GrafoDirigido:
    def __init__(self) -> None:
        self.grafo = {}
    
    def insertar_nodo(self, nodo):
        if nodo in self.grafo:
            print('El nodo ya existe en el grafo')
            return
        else:
            self.grafo[nodo]=[]
            
    def conectar_nodos(self, origen, destino):
        enlace = Enlace(origen,destino)
        ori= enlace.obtener_origen()
        des = enlace.obtener_destino()
        if ori not in self.grafo:
            raise ValueError(f'El nodo origen: {origen} no existe en el grafo')
        if des not in self.grafo:
            raise ValueError(f'El nodo destino: {destino} no existe en el grafo')
        self.grafo[ori].append(des)
        

    def imprimir(self):
        for clave, valor in self.grafo.items():
            print(f'Nodo: {clave} -----> {valor if valor else 'no tiene enlaces'}')
            
    
    
    def eliminar_nodo(self, nodo):
        if nodo in self.grafo:
            del self.grafo[nodo]
            for clave , valor in self.grafo.items():
                self.grafo[clave] = [x for x in valor if x != nodo]
        else:
            print(f'El nodo {nodo} no existe en el grafo')
            
            
    def dibujar_grafo(self):
        if self.grafo is None:
            return
        grafico = nx.DiGraph()
        grafico.add_nodes_from(list(self.grafo.keys()))
        for origen, destinos in self.grafo.items():
            for destino in destinos:
                grafico.add_edge(origen,destino)
                
        # Layout Spectral
        pos = nx.spectral_layout(grafico)
        plt.figure(figsize=(8,6),num='Mi Grafo')
        
        plt.title('Grafo Spectral')
        nx.draw(grafico, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='gray')
        plt.show()
        


lista_nodos = [47, 12, 83, 56, 91, 18, 35, 70,100]
graph = GrafoDirigido()

for i in lista_nodos:
    graph.insertar_nodo(i)


graph.conectar_nodos(47,35)
graph.conectar_nodos(47,91)
graph.conectar_nodos(18,35)
graph.conectar_nodos(70,12)
graph.conectar_nodos(12,18)
graph.conectar_nodos(35,70)
graph.conectar_nodos(12,83)
graph.conectar_nodos(12,70)
graph.conectar_nodos(56,18)
graph.conectar_nodos(56,100)
graph.conectar_nodos(91,100)


graph.dibujar_grafo()
