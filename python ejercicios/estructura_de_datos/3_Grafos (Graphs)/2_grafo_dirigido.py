# Ejercicio 2: Grafo Dirigido con Pesos
# Implementa una clase GrafoDirigido que represente un grafo dirigido con 
# pesos utilizando un diccionario de diccionarios para almacenar los nodos, 
# sus vecinos y los pesos de las aristas.


class GrafoDirigido:
    def __init__(self) -> None:
        self.nodos = {}
        
    def agregar_nodo(self, nodo):
        if nodo not in self.nodos:
            self.nodos[nodo]={}
    
    def agregar_arista(self, nodo1,nodo2, peso):
        if nodo1 in self.nodos and nodo2 in self.nodos:
            if nodo2 not in self.nodos[nodo1]:
                self.nodos[nodo1][nodo2] = peso            
            
    def imprimir_grafo(self):
        for nodo, vecinos in self.nodos.items():
            for vecino, peso in vecinos.items():
                print(f"Nodo {nodo} -> Nodo {vecino} (Peso: {peso})")


grafo_dirigido = GrafoDirigido()
grafo_dirigido.agregar_nodo(1)
grafo_dirigido.agregar_nodo(2)
grafo_dirigido.agregar_nodo(3)
grafo_dirigido.agregar_arista(1, 2, 5)
grafo_dirigido.agregar_arista(2, 3, 3)
grafo_dirigido.agregar_arista(3, 1, 2)
grafo_dirigido.agregar_arista(1, 3, 4) 
grafo_dirigido.imprimir_grafo()