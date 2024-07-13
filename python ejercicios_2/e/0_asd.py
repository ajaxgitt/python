import matplotlib.pyplot as plt
import networkx as nx

class Nodo:
    def __init__(self,valor) -> None:
        self.valor = valor
        self.siguiente = None
        

class ListaEnlazada:
    def __init__(self) -> None:
        self.primer_nodo = None
        
    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.primer_nodo is None:
            self.primer_nodo = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.primer_nodo
            self.primer_nodo = nuevo_nodo
            
    def imprimir(self):
        puntero = self.primer_nodo
        while puntero:
            print(puntero.valor , end=' -> ')
            puntero = puntero.siguiente
        print('fin')
    
    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.primer_nodo is None:
            self.primer_nodo  = nuevo_nodo
        else:
            puntero = self.primer_nodo
            while puntero.siguiente:
                puntero = puntero.siguiente
            puntero.siguiente = nuevo_nodo
        
    def eliminar(self, nodo):
        puntero = self.primer_nodo
        anterior = None
        if self.primer_nodo is None:
            print('lista vacia!!')
            return
        elif self.primer_nodo.valor == nodo:
            self.primer_nodo = self.primer_nodo.siguiente
            return
        else:
            while puntero:
                if puntero.valor == nodo:
                    print('nodo encontrado!!')
                    anterior.siguiente = puntero.siguiente
                    return
                anterior = puntero
                puntero = puntero.siguiente
            print('nodo Nodo encontrado!!')
            
            
    def dibujar_lista(self):
        grafico = nx.DiGraph()
        if self.primer_nodo is None:
            print('no existe ningun nodo!!')
            return
        else:
            puntero = self.primer_nodo
            x_position = 0
            while puntero is not None:
                grafico.add_node(puntero.valor, pos=(x_position, 0))
                x_position +=1
                if puntero.siguiente is not None:
                    grafico.add_edge(puntero.valor,puntero.siguiente.valor)
                puntero = puntero.siguiente
                
        pos = nx.get_node_attributes(grafico, 'pos')
        
        nx.draw(grafico,pos, with_labels= True, node_color = 'skyblue', edge_color ='gray',arrows=True)
        plt.show()
            
        
        
        
        
listaa = ListaEnlazada()
listaa.insertar_al_inicio(8)
listaa.insertar_al_inicio(7)
listaa.insertar_al_inicio(6)
listaa.imprimir()
listaa.insertar_al_final(0)
listaa.insertar_al_final(1)
listaa.insertar_al_final(2)
listaa.dibujar_lista()

listaa.imprimir()
listaa.eliminar(6)
listaa.imprimir()

listaa.dibujar_lista()