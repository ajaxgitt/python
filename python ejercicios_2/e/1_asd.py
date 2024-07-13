import matplotlib.pyplot as plt
import networkx as nx

class Nodo:
    def __init__(self,valor) -> None:
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
            self.primer_nodo =self.ultimo_nodo = nuevo_nodo
            return
        else:
            nuevo_nodo.siguiente = self.primer_nodo
            self.primer_nodo.anterior = nuevo_nodo
            self.primer_nodo = nuevo_nodo
            
    def imprimir(self):
        puntero = self.primer_nodo
        while puntero is not None:
            print(puntero.valor , end=' <--> ')
            puntero = puntero.siguiente
        print('fin')
            
    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.primer_nodo is None:
            self.primer_nodo =self.ultimo_nodo = nuevo_nodo
            return
        else:
            self.ultimo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.ultimo_nodo
            self.ultimo_nodo = nuevo_nodo
    
    def eliminar(self, nodo):
        puntero = self.primer_nodo
        if self.primer_nodo is None:
            print('lista vacia!!')
            return
        elif self.primer_nodo.valor == nodo:
            self.primer_nodo = self.primer_nodo.siguiente
        else:
            while puntero is not None:
                if puntero.valor == nodo:
                    puntero.anterior.siguiente = puntero.siguiente
                    return 
                puntero = puntero.siguiente
                
            
            
    
    def dibujar_lista(self):
        if self.primer_nodo is None:
            print('lista vacia!!')
            return
        else:
            grafico = nx.Graph()
            puntero = self.primer_nodo
            x = 0
            while puntero is not None:
                grafico.add_node(puntero.valor, pos=(x,0))
                x += 1
                if puntero.siguiente is not None:
                    grafico.add_edge(puntero.valor, puntero.siguiente.valor)
                puntero = puntero.siguiente
            pos = nx.get_node_attributes(grafico , 'pos')
            nx.draw(grafico,pos, with_labels = True, node_color = 'skyblue', edge_color = 'gray')
            plt.show()
        
        
        
        
        
listaa = ListaDoblementeEnlazada()
listaa.insertar_al_inicio(8)
listaa.insertar_al_inicio(7)
listaa.insertar_al_inicio(6)
listaa.imprimir()
listaa.insertar_al_final(0)
listaa.insertar_al_final(1)
listaa.insertar_al_final(2)
listaa.imprimir()
listaa.dibujar_lista()

listaa.eliminar(2)
listaa.imprimir()
listaa.dibujar_lista()


