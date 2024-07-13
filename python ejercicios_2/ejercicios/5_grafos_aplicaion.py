import matplotlib.pyplot as plt
import networkx as nx


class Nodo:
    def __init__(self, id, atributos :dict =None) -> None:
        self.id = id
        self.atributos = atributos if atributos is not None else {}

    def __repr__(self) -> str:
        return f'Nodo({self.id}, {self.atributos})'
    
    def __iter__(self):
        yield ('id',self.id)
        yield from self.atributos.items()
        


class Enlace:
    def __init__(self, origen, destino, peso=1) -> None:
        self.origen = origen
        self.destino = destino
        self.peso = peso

    def __repr__(self) -> str:
        return f'Enlace({self.origen.id} -> {self.destino.id}, peso={self.peso})'


class GrafoDirigido:

    def __init__(self) -> None:
        self.nodos = {}
        self.enlaces = []

    def agregar_nodo(self, nodo):
        if nodo.id not in self.nodos:
            self.nodos[nodo.id]=nodo
        else:
            print(f"El nodo con id {nodo.id} ya existe en el grafo.")
    
    def conectar_nodos(self, id_origen,id_destino, peso=1):
        if id_origen in self.nodos and id_destino in self.nodos:
            origen = self.nodos[id_origen]
            destino = self.nodos[id_destino]
            enlace = Enlace(origen,destino,peso)
            self.enlaces.append(enlace)
        else:
            print(f"Error: No se pueden conectar los nodos {id_origen} y {id_destino}. Al menos uno no existe.")
            
            
    def imprimir_nodos(self):
        print('Nodos')
        for _ , nodo in self.nodos.items():
            print(f'    {nodo}')
            
    def imprimir_enlaces(self):
        print('Enlaces')
        for i in self.enlaces:
            print(f'    {i}')
            
    def dibujar_grafo(self):
        if not self.nodos:
            print("El grafo no tiene nodos para dibujar.")
            return
        
        grafico = nx.DiGraph()
        
        for nodo in self.nodos.values():
            grafico.add_node(nodo.id, atributos=nodo.atributos)
            
            
        for enlace in self.enlaces:
            grafico.add_edge(enlace.origen.id, enlace.destino.id, peso=enlace.peso)
            
        # pos = nx.spring_layout(grafico)
        pos = nx.kamada_kawai_layout(grafico)
        
        plt.figure(figsize=(6,5), num='mi grafo')
        
        nx.draw(grafico, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='gray')
        edge_labels = nx.get_edge_attributes(grafico,'peso')
        nx.draw_networkx_edge_labels(grafico, pos, edge_labels=edge_labels)
        
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
grafo.conectar_nodos(1, 3, peso=2)
grafo.conectar_nodos(2, 3, peso=1)
grafo.conectar_nodos(3, 4, peso=4)
grafo.conectar_nodos(10, 4, peso=51)


# # Imprimir nodos y enlaces
# grafo.imprimir_nodos()
# grafo.imprimir_enlaces()

grafo.dibujar_grafo()