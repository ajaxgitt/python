import matplotlib.pyplot as plt
import networkx as nx


class Nodo:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.izquierda = None
        self.derecha = None



class Arbol:
    def __init__(self) -> None:
        self.root = None
    
    def insertar(self, nodo):
        if self.root is None:
            self.root = Nodo(nodo)
            return
        else:
            self._insertar(self.root, nodo)
    
    def _insertar(self, raiz , nodo):
        if nodo < raiz.valor:
            if raiz.izquierda is None:
                raiz.izquierda = Nodo(nodo)
            else:
                self._insertar(raiz.izquierda, nodo)
        else:
            if raiz.derecha is None:
                raiz.derecha = Nodo(nodo)
            else:
                self._insertar(raiz.derecha, nodo)
    
    
    def eliminar(self, nodo):
        self._eliminar(self.root, nodo)
        
        
    def _eliminar(self, raiz, nodo):
        if raiz is None:
            return None
        elif nodo < raiz.valor:
            raiz.izquierda = self._eliminar(raiz.izquierda,nodo)
        elif nodo > raiz.valor:
            raiz.derecha = self._eliminar(raiz.derecha, nodo)
        else:
            if raiz.izquierda is None:
                return raiz.derecha
            if raiz.derecha is None:
                return raiz.izquierda
            
            raiz.valor = self._buscar_menor(raiz.derecha).valor
            raiz.derecha = self._eliminar(raiz.derecha, raiz.valor)
        return raiz
    
    
    def _buscar_menor(self, nodo):
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo
    
    def ordenar_nodos(self):
        listaa = []
        return self._ordenar(self.root, listaa)
        
    def _ordenar(self, nodo, lista):
        if nodo:
            self._ordenar(nodo.izquierda, lista)
            lista.append(nodo.valor)
            self._ordenar(nodo.derecha, lista)
        return lista
            
            
    
    def insertar_datos(self, grafo, nodo, x = 0 , y = 0 , nivel=1, espaciado=1.5):
        if nodo is not None:
            grafo.add_node(nodo.valor, pos =(x, y))
            if nodo.izquierda is not None:
                grafo.add_edge(nodo.valor, nodo.izquierda.valor)
                self.insertar_datos(grafo, nodo.izquierda, x-espaciado/nivel, y-1, nivel+1, espaciado)
            if nodo.derecha is not None:
                grafo.add_edge(nodo.valor, nodo.derecha.valor)
                self.insertar_datos(grafo, nodo.derecha, x+espaciado/nivel, y-1, nivel+1, espaciado)
                
    
    def dibujar_arbol(self):
        grafico = nx.DiGraph()
        self.insertar_datos(grafico,self.root, espaciado=2)
        pos = nx.get_node_attributes(grafico, 'pos') 
        plt.figure(figsize=(8,9), num='mi arbol')
        nx.draw(grafico, pos, with_labels = True, node_color='skyblue', edge_color = 'gray', arrows=True, node_size=700)
        plt.show()




arbol = Arbol()

import random 
lista = []


for i in range(50):
    lista.append(random.randint(1,200))
lista = list(set(lista))
print(lista)


for i in lista:
    arbol.insertar(i)
    
#arbol.dibujar_arbol()

print(arbol.ordenar_nodos())