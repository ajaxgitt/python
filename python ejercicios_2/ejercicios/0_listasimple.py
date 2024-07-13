
import matplotlib.pyplot as plt
import networkx as nx


class Nodo:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.siguiente = None
        
class ListaEnlazadaSimple:
    def __init__(self) -> None:
        self.primer_nodo= None
    
    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.primer_nodo is None:
            self.primer_nodo = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.primer_nodo
            self.primer_nodo = nuevo_nodo
            
    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.primer_nodo is None:
            self.primer_nodo = nuevo_nodo
        else:
            puntero = self.primer_nodo
            while puntero.siguiente:
                puntero = puntero.siguiente
            puntero.siguiente = nuevo_nodo
    
    
    def imprimir_lista(self):
        puntero = self.primer_nodo
        while puntero:
            print(puntero.valor , end=' -> ')
            puntero = puntero.siguiente
        print('fin')
        
    def eliminar_nodo(self, nodo):
        if self.primer_nodo.valor == nodo:
            self.primer_nodo = self.primer_nodo.siguiente
        else:
            puntero = self.primer_nodo
            anterior = None
            while puntero:
                if puntero.valor == nodo:
                    anterior.siguiente = puntero.siguiente
                    return
                anterior = puntero
                puntero = puntero.siguiente
            print('Nodo no encontrado en la lista!!')
        
    def ista_nod(self):
        l = []
        puntero = self.primer_nodo
        while puntero:
            l.append(puntero.valor)
            puntero = puntero.siguiente
        return l
    
    
    def dibujar_lista(self):
        grafico = nx.DiGraph()
        lista_nodos = self.ista_nod() 
        x = 0
        puntero = self.primer_nodo
        while puntero:
            grafico.add_node(puntero.valor, pos=(x,0))
            puntero = puntero.siguiente
            x += 1
            
        for i in range(len(lista_nodos)-1):
            grafico.add_edge(lista_nodos[i],lista_nodos[i+1])
            
        pos = nx.get_node_attributes(grafico,'pos')
        nx.draw(grafico,pos, with_labels = True, node_color ='lightblue', edge_color= 'green', arrows = True)
        plt.show()
        




liista = ListaEnlazadaSimple()
liista.insertar_al_inicio(3)
liista.insertar_al_inicio(5)
liista.insertar_al_inicio(2)
liista.insertar_al_final(11)
liista.insertar_al_final(12)
liista.insertar_al_final(13)
liista.imprimir_lista()
liista.dibujar_lista()
liista.eliminar_nodo(5)
liista.eliminar_nodo(135)
liista.dibujar_lista()

            