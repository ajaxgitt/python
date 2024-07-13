# Ejercicio: Implementar una Lista Enlazada Simple
# Descripción:
# Vas a implementar una lista enlazada simple desde cero en Python. La lista enlazada debe permitir las siguientes operaciones:

# Agregar al inicio: Añadir un nuevo nodo al inicio de la lista.
# Agregar al final: Añadir un nuevo nodo al final de la lista.
# Eliminar un nodo: Eliminar un nodo que contenga un valor específico.
# Buscar un valor: Buscar si un valor específico está presente en la lista.
# Imprimir la lista: Imprimir todos los valores de la lista en orden.


class Nodo:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.siguiente =None
        
class ListaEnlazada:
    def __init__(self) -> None:
        self.primer_nodo = None
        
    def agregar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.primer_nodo is None:
            self.primer_nodo = nuevo_nodo
        else:
            nuevo_nodo.siguiente =self.primer_nodo
            self.primer_nodo = nuevo_nodo
            
    def agregar_final(self, dato):
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
            print(puntero.valor, end='-> ')
            puntero = puntero.siguiente
        print('fin')
        
    def eliminar(self, nodo):
        
        if self.primer_nodo is None:
            print('lista vacia!!')
            return
        elif self.primer_nodo.valor == nodo:
            puntero = self.primer_nodo.siguiente 
            self.primer_nodo = puntero
        else:
            self._eliminar(self.primer_nodo , nodo, contexto = None)
            
    def _eliminar(self, raiz , nodo, contexto):
        if raiz.siguiente is None:
            print(f'El nodo {nodo} no existe en la lista')
            return
        if raiz.valor == nodo:
            print(f'Nodo {nodo} eliminada ecitosamente!!')
            contexto.siguiente = raiz.siguiente 
            return 
        else:
            return self._eliminar(raiz.siguiente , nodo, raiz)

    def buscar(self, nodo):
        try:
            if self.primer_nodo.valor == nodo:
                print(f'Nodo {nodo} encontrado!!')
                return
            else:
                return self.buscar(self.primer_nodo.siguiente)
        except RecursionError:
            print('el nodo no se encuentra en la lista')

        
        








lista = ListaEnlazada()
lista.agregar_inicio(9)
lista.agregar_inicio(55)
lista.agregar_final(4)
lista.agregar_final(5)
lista.agregar_inicio(2)
lista.imprimir_lista()
lista.eliminar(55)
lista.imprimir_lista()
lista.buscar(652)

