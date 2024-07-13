

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

    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.primer_nodo is None:
            self.primer_nodo = self.ultimo_nodo = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.primer_nodo
            self.primer_nodo.anterior = nuevo_nodo
            self.primer_nodo = nuevo_nodo
            
    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.ultimo_nodo is None:
            self.primer_nodo = self.ultimo_nodo = nuevo_nodo
        else:
            self.ultimo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.ultimo_nodo
            self.ultimo_nodo = nuevo_nodo
            

    def imprimir(self):
        puntero = self.primer_nodo
        while puntero:
            print(puntero.valor, end=' <-> ')
            puntero = puntero.siguiente
        print('fin')

    def dibujar_lista(self):
        grafico = nx.Graph()
        lista_nodos = []
        puntero = self.primer_nodo
        
        posision_x = 0
        while puntero:
            lista_nodos.append(puntero.valor)
            
            grafico.add_node(puntero.valor, pos=(posision_x,0))
            posision_x +=1
            
            puntero = puntero.siguiente
            
        for i in range(len(lista_nodos)-1):
            grafico.add_edge(lista_nodos[i],lista_nodos[i+1])
        
        pos = nx.get_node_attributes(grafico, 'pos')
            
        nx.draw(grafico,pos,with_labels=True, node_color='lightblue', edge_color='green')
        plt.show()
        
    
        

listaa = ListaDoblementeEnlazada()
listaa.agregar_al_inicio(3)
listaa.agregar_al_inicio(6)
listaa.agregar_al_inicio(60)
listaa.imprimir()
listaa.agregar_al_final(33)
listaa.agregar_al_final(55)
listaa.agregar_al_final(11)
listaa.imprimir()
listaa.dibujar_lista()

