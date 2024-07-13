
import matplotlib.pyplot as plt
import networkx as nx


class Nodo:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        
class Enlaces:
    def __init__(self, nodo_origen,nodo_destino) -> None:
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

    def conectar_nodos(self, origen,destino):
        
        enlace = Enlaces(origen,destino)
        ori = enlace.obtener_origen()
        des = enlace.obtener_destino()
        
        if origen not in self.grafo:
            raise ValueError(f'El nodo {origen} no existe en el grafo')
        if destino not in self.grafo:
            raise ValueError(f'El nodo {origen} no existe en el grafo')
            
        self.grafo[ori].append(des)
        
    
    def eliminar_nodo(self,nodo):
        if nodo in self.grafo:
            del self.grafo[nodo]
            for key,value in self.grafo.items():
                self.grafo[key] = [x for x in value if x != nodo]
        else:
            print(f'El nodo {nodo} no existe en el grafo')
            
            
            
    def imprimir(self):
        for nodo,enlaces in self.grafo.items():
            print(f'Nodo: {nodo} ---> {enlaces}')
            
    def lista_nodos(self):
        return list(self.grafo.keys())
            
    def dibujar_grafo(self):
        if self.grafo is None:
            return
        grafico = nx.DiGraph()
        lista_nodos = self.lista_nodos()
        grafico.add_nodes_from(lista_nodos)
        for origen , destinos in self.grafo.items():
            for destino in destinos:
                grafico.add_edge(origen,destino)
            
        print("Nodos en el grafo:", grafico.nodes())
        
        #grafico 'Aleatorio'        
        # nx.draw(grafico, with_labels=True, node_color='skyblue', node_size=1500, edge_color='gray', arrows=True)
        # plt.show()     
        
        #grafico Circular
        pos = nx.circular_layout(grafico)
        nx.draw(grafico, pos=pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='gray')
        plt.show()

        
        
        
        
        
        
        
        
        
            
graph = GrafoDirigido()
graph.insertar_nodo(1)
graph.insertar_nodo(2)
graph.insertar_nodo(3)
graph.insertar_nodo(4)
graph.insertar_nodo(5)
graph.insertar_nodo(6)
graph.insertar_nodo(7)
graph.insertar_nodo(8)
graph.insertar_nodo(9)
graph.insertar_nodo(10)
graph.insertar_nodo(11)
graph.insertar_nodo(12)
graph.insertar_nodo(13)
graph.insertar_nodo(14)
graph.insertar_nodo(15)

print('Conexiones entre nodos:')
graph.conectar_nodos(2, 3)
graph.conectar_nodos(3, 4)
graph.conectar_nodos(4, 5)
graph.conectar_nodos(5, 1)
graph.conectar_nodos(5, 1)
graph.conectar_nodos(6, 5)
graph.conectar_nodos(15, 3)
graph.conectar_nodos(7, 6)
graph.conectar_nodos(7, 8)
graph.conectar_nodos(8, 9)
graph.conectar_nodos(7, 4)
graph.conectar_nodos(7, 15)
graph.conectar_nodos(9, 10)
graph.conectar_nodos(10, 6)
graph.conectar_nodos(7, 13)
graph.conectar_nodos(12, 13)
graph.conectar_nodos(13, 14)
graph.conectar_nodos(15, 11)


graph.eliminar_nodo(7)

graph.imprimir()
graph.dibujar_grafo()