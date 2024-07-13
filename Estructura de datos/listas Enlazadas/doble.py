import matplotlib.pyplot as plt
import networkx as nx



class Nodo:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self) -> None:
        self.primer_nodo = None
        self.ultimo_nodo = None
    
    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.primer_nodo is None:
            self.primer_nodo = self.ultimo_nodo = nuevo_nodo
            return
        else:
            nuevo_nodo.siguiente = self.primer_nodo
            self.primer_nodo.anterior = nuevo_nodo
            self.primer_nodo = nuevo_nodo
            return
        
    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.primer_nodo is None:
            self.primer_nodo = self.ultimo_nodo = nuevo_nodo
            return
        else:
            self.ultimo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.ultimo_nodo
            self.ultimo_nodo = nuevo_nodo
    
    def eliminar_nodo(self, nodo):
        if self.primer_nodo is None:
            print('lista vacia!!')
            return
        elif self.ultimo_nodo.valor == nodo:
            puntero = self.ultimo_nodo.anterior
            self.ultimo_nodo = puntero
            puntero.siguiente = None
            return
        elif self.primer_nodo.valor == nodo:
            puntero = self.primer_nodo.siguiente
            self.primer_nodo = puntero
            puntero.anterior = None
            return
        else:
            puntero = self.primer_nodo
            while puntero:
                if puntero.valor == nodo:
                    puntero.anterior.siguiente = puntero.siguiente
                    return
                puntero = puntero.siguiente
            print(f'El nodo {nodo} no existe en la lista')
                
    
    def dibujar_lista(self):
        if self.primer_nodo is None:
            print('lista vacia!!')
            return
        else:
            grafico = nx.Graph()
            x = 0
            puntero = self.primer_nodo
            while puntero:
                grafico.add_node(puntero.valor, pos=(x, 0))
                x += 1
                if puntero.siguiente is not None:
                    
                    grafico.add_edge(puntero.valor, puntero.siguiente.valor)
                puntero = puntero.siguiente
                
            pos = nx.get_node_attributes(grafico, 'pos')
            nx.draw(grafico, pos, with_labels = True, node_color = 'skyblue', edge_color = 'gray')
            plt.show()
    
    
    
    
    
    
lista = ListaDoblementeEnlazada()
lista.insertar_al_inicio(10)
lista.insertar_al_inicio(20)
lista.insertar_al_inicio(30)
lista.insertar_al_final(3)
lista.insertar_al_final(2)
lista.insertar_al_final(1)
lista.dibujar_lista()
lista.eliminar_nodo(2)
lista.dibujar_lista()