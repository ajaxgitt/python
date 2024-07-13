
import matplotlib.pyplot as plt
import networkx as nx


class Nodo:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.izquierda = None
        self.derecha = None
    def __str__(self) -> str:
        return str(self.valor)
        

class ArbolesBusquedaBinaria:
    def __init__(self) -> None:
        self.root = None
        
    def insertar(self, dato):
        if self.root is None:
            self.root = Nodo(dato)
        else:
            self._insertar(self.root, dato)
        
    def _insertar(self, nodo , dato):
        if dato < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self._insertar(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self._insertar(nodo.derecha, dato)
    def recorrido_inorden(self):
        self._recorrido_inorden(self.root)        
        
    def _recorrido_inorden(self, nodo):
        if nodo:
            self._recorrido_inorden(nodo.izquierda)
            print(nodo.valor)
            self._recorrido_inorden(nodo.derecha)
            

    def _agregar_nodos_aristas(self, grafo, nodo, x=0,y=0, nivel=1, espaciado=1.5):
        if nodo is not None:
            grafo.add_node(nodo.valor, pos=(x,y))
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
        plt.figure(figsize=(8, 6))
        nx.draw(grafico, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_color='black', edge_color='grey', arrows=False)
        plt.show()
        
    def eliminar(self, dato):
        self._eliminar(self.root, dato)
        
    def _eliminar(self, nodo, dato):
        if nodo is None:
            return None
        elif dato < nodo.valor:
            nodo.izquierda = self._eliminar(nodo.izquierda, dato)
        elif dato > nodo.valor:
            nodo.derecha = self._eliminar(nodo.derecha, dato)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            nodo.valor = self._buscar_menor(nodo.derecha).valor
            nodo.derecha = self._eliminar(nodo.derecha, nodo.valor)
        return nodo
        
    def _buscar_menor(self, nodo):
        puntero = nodo
        while puntero.izquierda:
            puntero = puntero.izquierda
        return puntero
    
    def buscar_nodo(self, dato):
        self._buscar_nodo(self.root, dato)
        
    def _buscar_nodo(self, nodo, dato):
        if nodo is None:
            print(f'El {dato} no se encuentra en el arbol')
            return
        if nodo.valor == dato:
            print(f'Nodo {dato} encontrado!!')
            return
        if dato < nodo.valor:
            self._buscar_nodo(nodo.izquierda,dato)
        else:
            self._buscar_nodo(nodo.derecha, dato)

arbol = ArbolesBusquedaBinaria()
arbol.insertar(10)  
arbol.insertar(5)   
arbol.insertar(15)  

arbol.insertar(2)  
arbol.insertar(23)    
arbol.insertar(11)    
arbol.insertar(13)   
arbol.insertar(19)   

arbol.buscar_nodo(2)

arbol.insertar(3)    
arbol.insertar(7)    
arbol.insertar(12)   
arbol.insertar(18)   
arbol.insertar(90)   
arbol.insertar(92)
arbol.insertar(89)   
arbol.insertar(10.5)  
arbol.recorrido_inorden()
arbol.dibujar_arbol()

arbol.eliminar(10)
arbol.dibujar_arbol()





# arbol.recorrido_inorden()
# arbol.dibujar_arbol()
