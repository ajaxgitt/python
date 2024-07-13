import matplotlib.pyplot as plt
import networkx as nx






class Nodo:
    def __init__(self, valor) -> None:
        self.valor =valor
        self.siguiente = None
        

class listaEnlasadaSimple:
    
    def __init__(self) -> None:
        self.primer_nodo = None
        
    def insertar_al_inicio(self,dato):
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
            
    def lista(self):
        grafico = nx.DiGraph()
        
        lista = []
        puntero = self.primer_nodo
        x_position = 0
        while puntero:
            lista.append(puntero.valor)
            
            grafico.add_node(puntero.valor, pos=(x_position, 0))
            x_position += 1
            puntero = puntero.siguiente

        for i in range(len(lista)-1):
            grafico.add_edge(lista[i], lista[i+1])
        
        pos = nx.get_node_attributes(grafico, 'pos')
        nx.draw(grafico, pos, with_labels=True, node_color='lightblue', edge_color='green', arrows=True)
        plt.show()
            
            
    def imprimir(self):
        puntero = self.primer_nodo
        while puntero:
            print(puntero.valor, end=' -> ')
            puntero = puntero.siguiente
        print('fin')
        








listaEn = listaEnlasadaSimple()
listaEn.insertar_al_inicio(9)
listaEn.insertar_al_inicio(8)
listaEn.insertar_al_inicio(0)



listaEn.imprimir()
listaEn.insertar_al_final(10)
listaEn.insertar_al_final(20)
listaEn.insertar_al_inicio(11)
listaEn.imprimir()
listaEn.lista()


