import matplotlib.pyplot as plt
import networkx as nx


class Nodo:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class ArbolBusquedaBinaria:
    def __init__(self) -> None:
        self.root = None

    def insertar(self, dato):
        if self.root is None:
            self.root = Nodo(dato)
            return
        else:
            self._insertar(self.root, dato)

    def _insertar(self, raiz, nodo):
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

    def in_order(self):
        self._in_order(self.root)

    def _in_order(self, nodo):
        if nodo:
            self._in_order(nodo.izquierda)
            print(nodo.valor)
            self._in_order(nodo.derecha)
            
    def eliminar(self, dato):
        self._eliminar(self.root, dato)
        
    def _eliminar(self, raiz, nodo):
        if raiz is None:
            return None
        elif nodo < raiz.valor:
            raiz.izquierda = self._eliminar(raiz.izquierda, nodo)
        elif nodo > raiz.valor:
            raiz.derecha = self._eliminar(raiz.derecha, nodo)
        else:
            if raiz.izquierda is None:
                return raiz.derecha
            elif raiz.derecha is None:
                return raiz.izquierda
            
            raiz.valor = self._buscar_menor(raiz.derecha).valor
            raiz.derecha = self._eliminar(raiz.derecha, raiz.valor)
        
        return raiz        
    
    def _buscar_menor(self, nodo):
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo
        
        
        

    def _agregar_nodos_aristas(self, grafo, nodo, x=0, y=0, nivel=1, espaciado=1.5):
        if nodo is not None:
            grafo.add_node(nodo.valor, pos=(x, y))
            if nodo.izquierda is not None:
                grafo.add_edge(nodo.valor, nodo.izquierda.valor)
                self._agregar_nodos_aristas(grafo, nodo.izquierda, x-espaciado/nivel,y-1,nivel+1,espaciado)
            if nodo.derecha is not None:
                grafo.add_edge(nodo.valor, nodo.derecha.valor)
                self._agregar_nodos_aristas(grafo, nodo.derecha, x+espaciado/nivel,y-1,nivel+1,espaciado)
                        

    def dibujar_arbol(self):
        if self.root is None:
            return
        grafico = nx.DiGraph()
        self._agregar_nodos_aristas(grafico,self.root, espaciado=2)
        pos = nx.get_node_attributes(grafico, 'pos')
        plt.figure(figsize=(8,6))
        nx.draw(grafico, pos,with_labels = True,node_size=700,node_color='skyblue', edge_color = 'gray',arrows=True)
        plt.show()
        
    


arbol = ArbolBusquedaBinaria()
arbol.insertar(9)
arbol.insertar(8)
arbol.insertar(69)
arbol.insertar(35)
arbol.insertar(32)
arbol.insertar(6)
arbol.insertar(7)
arbol.insertar(70)
arbol.insertar(8.5)

arbol.insertar(5)

arbol.in_order()
arbol.dibujar_arbol()

arbol.eliminar(9)
arbol.dibujar_arbol()
