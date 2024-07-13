import matplotlib.pyplot as plt
import networkx as nx


class Nodo:
    def __init__(self, id , atributos=None) -> None:
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
        
    def obtener_numero_nodos(self):
        print(f'{len(self.nodos.keys())} nodos')
        return 
        
    def obtener_numero_enlaces(self):
        print(f'{len(self.enlaces)} enlaces')
        return
    
    def agregar_nodo(self, nodo):
        if nodo.id not in  self.nodos:
            self.nodos[nodo.id]= nodo
        else:
            print(f'El nodo con el id {nodo.id} ya existe en el grafo.!')
    
    def conectar_nodos(self, id_origen,id_destino, peso=1):
        if id_origen in self.nodos and id_destino in self.nodos:
            origen = self.nodos[id_origen]
            destino = self.nodos[id_destino]
            enlace = Enlace(origen,destino, peso)
            self.enlaces.append(enlace)
        else:
            print(f"Error: No se pueden conectar los nodos {id_origen} y {id_destino}. Al menos uno no existe.")
            
    def imprimir_enlaces(self):
        for i in self.enlaces:
            print(i)
            
    def imprimir_nodos(self):
        for _, valor in self.nodos.items():
            print(f'{valor}')
    
    
    def dibujar_grafo(self, layout='kamada_kawai'):
        if not self.nodos:
            print("El grafo no tiene nodos para dibujar.")
            return
        
        grafico = nx.DiGraph()
        for nodo in self.nodos.values():
            grafico.add_node(nodo.id)
            
        for enlace in self.enlaces:
            grafico.add_edge(enlace.origen.id, enlace.destino.id, peso=enlace.peso)
        layout == 'spectral'
        pos = nx.spectral_layout(grafico)
        plt.figure(figsize=(12,10))
        nx.draw(grafico, pos, with_labels=True, labels=nx.get_node_attributes(grafico, 'label'),
                node_color='skyblue', node_size=10, edge_color='gray', font_size=10)
        pesos = nx.get_edge_attributes(grafico, 'peso')
        nx.draw_networkx_edge_labels(grafico, pos, edge_labels=pesos)
        plt.show()
        
