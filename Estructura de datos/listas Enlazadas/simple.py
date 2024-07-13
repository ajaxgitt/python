import matplotlib.pyplot as plt
import networkx as nx



class Nodo:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.siguiente = None
        
class ListaSimple:
    def __init__(self) -> None:
        self.primer_nodo = None
        
    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.primer_nodo is None:
            self.primer_nodo = nuevo_nodo
            return 
        else:
            nuevo_nodo.siguiente = self.primer_nodo
            self.primer_nodo = nuevo_nodo
    
    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.primer_nodo is None:
            self.primer_nodo = nuevo_nodo
            return
        else:
            puntero = self.primer_nodo
            while puntero.siguiente:
                puntero = puntero.siguiente
            puntero.siguiente = nuevo_nodo
    
    def eliminar_nodo(self, nodo):
        if self.primer_nodo is None:
            print('lista vacia!!')
            return
        elif self.primer_nodo.valor == nodo:
            self.primer_nodo = self.primer_nodo.siguiente
            return
        else:
            anterior = None
            puntero = self.primer_nodo
            while puntero:
                if puntero.valor == nodo:
                    anterior.siguiente = puntero.siguiente
                    print(f'nodo {nodo} eliminado con exito!!')
                    return
                anterior = puntero
                puntero = puntero.siguiente
            print(f'nodo {nodo} no encontrado!!')
            
    def dibujar_lista(self):
        if self.primer_nodo is None:
            print('lista vacia!!')
            return
        else:
            grafico = nx.DiGraph()
            puntero = self.primer_nodo
            x = 0
            while puntero is not None:
                grafico.add_node(puntero.valor, pos = (x,0))
                x +=1
                if puntero.siguiente is not None:
                    grafico.add_edge(puntero.valor, puntero.siguiente.valor)
                puntero = puntero.siguiente
            
            
            pos = nx.get_node_attributes(grafico, 'pos')
            nx.draw(grafico,pos, with_labels = True,node_color ='skyblue', edge_color = 'gray', arrows = True )
            plt.show()
            


lista = ListaSimple()
lista.insertar_al_inicio(10)
lista.insertar_al_inicio(20)
lista.insertar_al_inicio(30)
lista.insertar_al_final(3)
lista.insertar_al_final(2)
lista.insertar_al_final(1)
lista.dibujar_lista()
lista.eliminar_nodo(30)
lista.dibujar_lista()
    
        
                
                
            