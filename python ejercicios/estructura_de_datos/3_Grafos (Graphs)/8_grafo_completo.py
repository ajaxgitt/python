
import networkx as nx
import matplotlib.pyplot as plt


class Nodo:
    def __init__(self, id, atributos=None):
        self.id = id
        self.atributos = atributos if atributos is not None else {}

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

    def agregar_nodo(self, nodo):
        if nodo.id not in self.nodos:
            self.nodos[nodo.id] = nodo
        else:
            print(f'El nodo con el id {nodo.id} ya existe en el grafo.!')

    def conectar_nodos(self, id_origen, id_destino, peso=1):
        if id_origen in self.nodos and id_destino in self.nodos:
            nodo_origen = self.nodos[id_origen]
            nodo_destino = self.nodos[id_destino]
            enlace = Enlace(nodo_origen,nodo_destino,peso)
            self.enlaces.append(enlace)
        else:
            print(f"Error: No se pueden conectar los nodos {id_origen} y {id_destino}. Al menos uno no existe.")

            
    def imprimir_enlaces(self):
        for i in self.enlaces:
            print(i)
            
    def imprimir_nodos(self):
        for _, valor in self.nodos.items():
            print(f'{valor}')
    
    def elminar_nodo(self, nodo_id):
        if nodo_id in self.nodos:
            del self.nodos[nodo_id]
            self.enlaces = [x for x in self.enlaces if x.origen.id != nodo_id and x.destino.id != nodo_id]
        else:
            print(f'El nodo con el id {nodo_id} no existe en el grafo.!')
            
            
    def dibujar_grafo(self):
        if not self.nodos:
            print("El grafo no tiene nodos para dibujar.")
            return
        grafico = nx.DiGraph()
        for i in self.nodos.values():
            grafico.add_node(i.id)
            
        for enlace in self.enlaces:
            grafico.add_edge(enlace.origen.id , enlace.destino.id, peso = enlace.peso)
        
        pos = nx.kamada_kawai_layout(grafico)
        plt.figure(figsize=(6,5))
        nx.draw(grafico,pos,with_labels=True,node_color = 'skyblue',node_size=500,edge_color='gray')
        lables = nx.get_edge_attributes(grafico,'peso')
        nx.draw_networkx_edge_labels(grafico,pos,lables)
        plt.show()
            

grafo = GrafoDirigido()

# Agregar nodos
nodo1 = Nodo(1, {'tipo': 'A'})
nodo2 = Nodo(2, {'tipo': 'B'})
nodo3 = Nodo(3, {'tipo': 'C'})
nodo4 = Nodo(4, {'tipo': 'A'})
nodo5 = Nodo(10,{'nombre':'yecid','edad':25})

grafo.agregar_nodo(nodo1)
grafo.agregar_nodo(nodo2)
grafo.agregar_nodo(nodo3)
grafo.agregar_nodo(nodo4)
grafo.agregar_nodo(nodo5)

# Conectar nodos
grafo.conectar_nodos(1, 2, peso=3)
grafo.conectar_nodos(3, 4, peso=4)
grafo.conectar_nodos(10, 3, peso=51)
grafo.conectar_nodos(2, 4, peso=11)
grafo.conectar_nodos(4, 1, peso=11)


grafo.dibujar_grafo()
grafo.elminar_nodo(1)
grafo.dibujar_grafo()
grafo.elminar_nodo(10)
grafo.dibujar_grafo()






