import re
from turtle import pos, pu
import networkx as nx
import matplotlib.pyplot as plt
from networkx import get_edge_attributes


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

    def __str__(self) -> str:
        return str(self.valor)


class listaDoblementeEnlazada:
    def __init__(self) -> None:
        self.primer_nodo = None
        self.ultimo_nodo = None

    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.primer_nodo is None:
            self.primer_nodo = self.ultimo_nodo = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.primer_nodo
            self.primer_nodo.anterior = nuevo_nodo
            self.primer_nodo = nuevo_nodo

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.ultimo_nodo is None:
            self.ultimo_nodo = self.primer_nodo = nuevo_nodo
        else:
            self.ultimo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.ultimo_nodo
            self.ultimo_nodo = nuevo_nodo

    def dibujar_lista(self):
        grafico = nx.Graph()
        puntero = self.primer_nodo
        lista = []
        x = 0
        while puntero:
            lista.append(puntero.valor)
            grafico.add_node(puntero.valor, pos=(x, 0))
            x += 1
            puntero = puntero.siguiente

        for i in range(len(lista)-1):
            grafico.add_edge(lista[i], lista[i+1])

        pos = nx.get_node_attributes(grafico, 'pos')

        nx.draw(grafico, pos, with_labels=True,
                node_color='lightblue', edge_color='green')
        plt.show()

    def eliminar(self, nodo):
        puntero = self.primer_nodo
        if puntero.valor == nodo:
            self.primer_nodo.anterior = None
            self.primer_nodo = self.primer_nodo.siguiente
            return
        while puntero:
            if self.ultimo_nodo.valor == nodo:
                self.ultimo_nodo.anterior.siguiente = None
                self.ultimo_nodo = self.ultimo_nodo.anterior
                return
            if puntero.valor == nodo:
                puntero.anterior.siguiente = puntero.siguiente
                puntero.siguiente.anterior = puntero.anterior
                return
            puntero = puntero.siguiente
        print('Nose encontro dicho nodo!!')


liiista = listaDoblementeEnlazada()
liiista.insertar_al_inicio(5)
liiista.insertar_al_inicio(4)
liiista.insertar_al_inicio(3)
liiista.insertar_al_final(2)
liiista.insertar_al_final(1)
liiista.insertar_al_final(0)
liiista.dibujar_lista()
liiista.eliminar(0)
liiista.dibujar_lista()
liiista.eliminar(1)
liiista.eliminar(3)
liiista.dibujar_lista()
liiista.eliminar(5)
liiista.dibujar_lista()


