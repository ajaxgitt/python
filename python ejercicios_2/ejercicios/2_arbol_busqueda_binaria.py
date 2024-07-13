
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
        else:
            self._insertar(self.root, dato)

    def _insertar(self, nodo, dato):
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

    def eliminar(self, nodo_a_eliminar):
        self._eliminar(self.root, nodo_a_eliminar)

    def _eliminar(self, raiz, nodo):
        if raiz is None:
            return None
        #buscamos de manera recursiva el nodo
        elif nodo < raiz.valor:
            raiz.izquierda = self._eliminar(raiz.izquierda,nodo)
        elif nodo > raiz.valor:
            raiz.derecha = self._eliminar(raiz.derecha, nodo)
        else:
            #nodo encontrado
            #encaso de que el nodo encontrado tenfa un hijo devolvemos el nodo 
            if raiz.izquierda is None:
                return raiz.derecha
            elif raiz.derecha is None:
                return raiz.izquierda
            raiz.valor = self._buscar_menor(raiz.derecha).valor
            raiz.derecha = self._eliminar(raiz.derecha,raiz.valor)
        return raiz
            
            
            
            
    def _buscar_menor(self, nodo):
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo
    
    def _agregar_nodos_aristas(self, grafo, nodo, x=0 , y=0, nivel=1, espaciado=1.5):
        if nodo:
            grafo.add_node(nodo.valor, pos=(x,y))
            if nodo.izquierda:
                grafo.add_edge(nodo.valor, nodo.izquierda.valor)
                self._agregar_nodos_aristas(grafo, nodo.izquierda, x-espaciado/nivel,y-1, nivel+1, espaciado)
            if nodo.derecha:
                grafo.add_edge(nodo.valor, nodo.derecha.valor)
                self._agregar_nodos_aristas(grafo, nodo.derecha, x+espaciado/nivel,y-1, nivel+1, espaciado)
            
    def dibujar_arbol(self):
        if self.root is None:
            return None
        grafico = nx.DiGraph()
        self._agregar_nodos_aristas(grafico,self.root, espaciado=2)
        pos = nx.get_node_attributes(grafico,'pos')
        
        plt.figure(figsize=(8,6),num='Mi Arbol')
        plt.title('Arbol busqueda binaria')
        
        nx.draw(grafico,pos, with_labels = True, node_size=700, node_color = 'lightblue', font_size = 10, font_color ='black', edge_color='green',arrows=True)
        plt.show()
        
        


arbol = ArbolBusquedaBinaria()
arbol.insertar(10)
arbol.insertar(60)
arbol.insertar(30)
arbol.insertar(400)
arbol.insertar(1)
arbol.insertar(6)
arbol.insertar(3)
arbol.insertar(8)
arbol.insertar(0)
arbol.insertar(20)
arbol.insertar(25)
arbol.insertar(28)

arbol.dibujar_arbol()

arbol.recorrido_inorden()
arbol.eliminar(10)
print('------------')
arbol.recorrido_inorden()
arbol.dibujar_arbol()



