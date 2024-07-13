import networkx as nx
import matplotlib.pyplot as plt



class Nodo:
    def __init__(self,nombre) -> None:
        self.nombre = nombre
        
        
class Enlace:
    def __init__(self,origen,destino, peso) -> None:
        self.origen = origen
        self.destino = destino
        self.peso = peso
        
    def obtener_origen(self):
        return self.origen
    
    def obtener_destino(self):
        return self.destino
    
    def obtener_peso(self):
        return self.peso
    

        
class GrafoDirigido:
    def __init__(self) -> None:
        self.grafo = {}
    
    def insertar_nodo(self, dato):
        nuevo_nodo = Nodo(dato)
        if not dato in self.grafo:
            self.grafo[nuevo_nodo.nombre]={}
            
    def conectar_nodos(self, nodo_origen,nodo_destino,peso):
        if nodo_origen in self.grafo and  nodo_destino in self.grafo:
            nuevo_enlace = Enlace(nodo_origen, nodo_destino,peso)
            self.grafo[nuevo_enlace.origen][nuevo_enlace.destino]= nuevo_enlace.peso
            
    def imprimir(self):
        print(self.grafo.keys())
        for nodo,enlaces in self.grafo.items():
            for i in enlaces.items():
                print(f'Nodo: {nodo} ---> {i}')
                
    def lista_nodos(self):
        return list(self.grafo.keys())
            
    def dibujar_grafo(self):
        if self.grafo is None:
            return
        
        grafico = nx.DiGraph()
        lista_nodos = self.lista_nodos()
        grafico.add_nodes_from(lista_nodos)
        
        for origen , destinos in self.grafo.items():
            for destino , peso in destinos.items():
                grafico.add_edge(origen,destino, weight= peso)
            
        print("Nodos en el grafo:", grafico.nodes())
        # nx.draw(grafico, with_labels=True, node_color='skyblue', node_size=1500, edge_color='gray', arrows=True)
        # plt.show()     
        
        #grafico Circular
        pos = nx.spring_layout(grafico)  # Posiciones de los nodos
        nx.draw(grafico, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=16, font_color='black')

        # Añadir etiquetas de peso a los bordes
        labels = nx.get_edge_attributes(grafico, 'weight')
        nx.draw_networkx_edge_labels(grafico, pos, edge_labels=labels, font_color='red')

        plt.show()
                    
graph = GrafoDirigido()
graph.insertar_nodo(1)
graph.insertar_nodo(2)
graph.insertar_nodo(3)
graph.insertar_nodo(6)
graph.insertar_nodo(7)
graph.insertar_nodo(8)
graph.insertar_nodo(9)
graph.insertar_nodo(10)


graph.conectar_nodos(2, 3,5)
graph.conectar_nodos(3, 1,9)
graph.conectar_nodos(1, 2,33)

graph.conectar_nodos(6, 7,5)
graph.conectar_nodos(7, 3,9)
graph.conectar_nodos(8, 6,33)
graph.conectar_nodos(9, 1,5)
graph.conectar_nodos(10, 1,9)
graph.conectar_nodos(6, 10,33)
            
graph.imprimir()
graph.dibujar_grafo()