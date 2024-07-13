import matplotlib.pyplot as plt
import networkx as nx

class Nodo:
    def __init__(self, id, atributos=None):
        self.id = id
        self.atributos = atributos if atributos is not None else {}

    def __repr__(self):
        return f"Nodo({self.id}, {self.atributos})"

    # def __str__(self):
    #     return f"Nodo ID: {self.id}, Atributos: {self.atributos}"


class Enlace:
    def __init__(self, origen, destino, peso=1):
        self.origen = origen
        self.destino = destino
        self.peso = peso

    def __repr__(self):
        return f"Enlace({self.origen.id} -> {self.destino.id}, peso={self.peso})"


class GrafoDirigido:
    def __init__(self):
        self.nodos = {}
        self.enlaces = []

    def agregar_nodo(self, nodo):
        if nodo.id not in self.nodos:
            self.nodos[nodo.id] = nodo
        else:
            print(f"El nodo con id {nodo.id} ya existe en el grafo.")

    def conectar_nodos(self, id_origen, id_destino, peso=1):
        if id_origen in self.nodos and id_destino in self.nodos:
            origen = self.nodos[id_origen]
            destino = self.nodos[id_destino]
            enlace = Enlace(origen, destino, peso)
            self.enlaces.append(enlace)
        else:
            print(f"Error: No se pueden conectar los nodos {id_origen} y {id_destino}. Al menos uno no existe.")

    def imprimir_nodos(self):
        print("Nodos:")
        for nodo_id, nodo in self.nodos.items():
            print(f'  {nodo}')


    def imprimir_enlaces(self):
        print("Enlaces:")
        for enlace in self.enlaces:
            print(f"  {enlace}")

    def dibujar_grafo(self):
        if not self.nodos:
            print("El grafo no tiene nodos para dibujar.")
            return

        grafico = nx.DiGraph()

        # Agregar nodos al grafo de NetworkX
        for nodo in self.nodos.values():
            # grafico.add_node(nodo.id, atributos=nodo.atributos)
            grafico.add_node(nodo.id, atributos=nodo.atributos)
            #grafico.add_node(nodo.id)

        # Agregar enlaces al grafo de NetworkX
        for enlace in self.enlaces:
            grafico.add_edge(enlace.origen.id, enlace.destino.id, peso=enlace.peso)

        # Obtener posiciones de los nodos
        pos = nx.spring_layout(grafico)

        # Dibujar el grafo
        plt.figure(figsize=(6,5),num='Mi Grafo')
        
        nx.draw(grafico, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=12, font_color='black', edge_color='green', arrows=True)

        # Mostrar los atributos de los nodos
        node_labels = nx.get_node_attributes(grafico, 'atributos')
        nx.draw_networkx_labels(grafico, pos, labels=node_labels)

        # Mostrar pesos de los enlaces
        edge_labels = nx.get_edge_attributes(grafico, 'peso')
        nx.draw_networkx_edge_labels(grafico, pos, edge_labels=edge_labels)

        # Añadir título al grafo
        plt.title('Grafo Dirigido con NetworkX')

        # Mostrar el grafo
        plt.show()


grafo = GrafoDirigido()

# Agregar nodos
nodo1 = Nodo(1, {'tipo': 'A'})
nodo2 = Nodo(2, {'tipo': 'B'})
nodo3 = Nodo(3, {'tipo': 'C'})
nodo4 = Nodo(4, {'tipo': 'A'})

grafo.agregar_nodo(nodo1)
grafo.agregar_nodo(nodo2)
grafo.agregar_nodo(nodo3)
grafo.agregar_nodo(nodo4)

# Conectar nodos
grafo.conectar_nodos(1, 2, peso=3)
grafo.conectar_nodos(1, 3, peso=2)
grafo.conectar_nodos(2, 3, peso=1)
grafo.conectar_nodos(3, 4, peso=4)

# Imprimir nodos y enlaces
grafo.imprimir_nodos()
grafo.imprimir_enlaces()

# Dibujar el grafo
grafo.dibujar_grafo()
