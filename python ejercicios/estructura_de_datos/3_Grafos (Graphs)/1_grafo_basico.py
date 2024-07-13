
#Implementa una clase Grafo que represente un grafo no dirigido 
# utilizando un diccionario para almacenar los nodos y sus vecinos.



class Grafo:
    def __init__(self) -> None:
        self.nodos = {}
        
    def agregar_nodo(self, nodo):
        if nodo not in self.nodos:
            self.nodos[nodo]=[]
            
    def agregar_arista(self, nodo1,nodo2):
        if nodo1 in self.nodos and nodo2 in self.nodos:
            if nodo2 not in self.nodos[nodo1]:
                self.nodos[nodo1].append(nodo2)
            if nodo1 not in self.nodos[nodo2]:
                self.nodos[nodo2].append(nodo1)
                
    def imprimir_grafo(self):
        for nodo , vecinos in self.nodos.items():
            print(f"Nodo {nodo}: {vecinos}")
            
            
grafo = Grafo()
grafo.agregar_nodo(1)
grafo.agregar_nodo(2)
grafo.agregar_nodo(3)
grafo.agregar_nodo(4)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 1)
grafo.agregar_arista(1, 4)
grafo.imprimir_grafo()