# Ejercicio: Implementar y manipular una lista doblemente enlazada
# Instrucciones:
# Implementa las siguientes operaciones en una clase ListaDobleEnlazada:

# Insertar un nodo al inicio (insertar_al_inicio)
# Insertar un nodo al final (insertar_al_final)
# Eliminar un nodo al inicio (eliminar_del_inicio)
# Eliminar un nodo al final (eliminar_del_final)
# Buscar un nodo por valor (buscar)
# Mostrar la lista en orden desde el inicio (mostrar_desde_inicio)
# Mostrar la lista en orden desde el final (mostrar_desde_final)
# Escribe un código de prueba para demostrar que todas las operaciones funcionan correctamente.



class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None
        
    def __str__(self) -> str:
        return str(self.valor)
        

class ListaDobleEnlazada:
    
    def __init__(self) -> None:
        self.primer_nodo = None
        self.ultimo_nodo = None
    
    def insertar_al_inicio(self, nodo_valor):
        nuevo_nodo = Nodo(nodo_valor)
        if self.primer_nodo is None:
            self.primer_nodo = self.ultimo_nodo = nuevo_nodo
        else:
            puntero = self.primer_nodo
            puntero.anterior = nuevo_nodo
            nuevo_nodo.siguiente = puntero
            self.primer_nodo = nuevo_nodo
            return
    
    def insertar_al_final(self,nodo_valor):
        nuevo_nodo = Nodo(nodo_valor)
        if self.ultimo_nodo is None:
            self.primer_nodo = self.ultimo_nodo = nuevo_nodo
            return
        else:
            puntero = self.ultimo_nodo
            puntero.siguiente = nuevo_nodo
            nuevo_nodo.anterior = puntero
            self.ultimo_nodo = nuevo_nodo
            
            return
    
    def mostrar_desde_inicio(self):
        if self._verificar() is True:
            return
        puntero = self.primer_nodo
        while puntero:
            print(puntero.valor , end=' -> ')
            puntero = puntero.siguiente
        print('fin!!')
        return
    
    def mostrar_desde_final(self):
        if self._verificar() is True:
            return
        puntero = self.ultimo_nodo
        while puntero:
            print(puntero.valor , end=' -> ')
            puntero = puntero.anterior
        print('fin!!')
    
    def eliminar_del_inicio(self):
        if self.primer_nodo is None:
            print('fin')
            return
        else:
            puntero = self.primer_nodo.siguiente
            puntero.anterior = None
            self.primer_nodo = puntero
        
    def eliminar_del_final(self):
        if self.ultimo_nodo is None:
            print('fin')
            return
        else:
            puntero = self.ultimo_nodo.anterior
            puntero.siguiente = None
            self.ultimo_nodo = puntero
        
        
    def buscar(self,nodo_valor):
        puntero = self.primer_nodo
        if self._verificar() is True:
            return
        else:
            while puntero:
                if puntero.valor == nodo_valor:
                    return True
                puntero = puntero.siguiente
            return False
        
    
    def _verificar(self):
        if self.primer_nodo is None:
            print('la lista esta vacia!!')
            return
    
# # # Prueba de las operaciones
lista = ListaDobleEnlazada()
lista.insertar_al_inicio(5)
lista.insertar_al_inicio(36)
lista.insertar_al_inicio(6)
lista.insertar_al_inicio(8)

lista.mostrar_desde_inicio()  # Salida: 0 1 2
lista.eliminar_del_inicio()
lista.mostrar_desde_inicio()  # Salida: 0 1 2

lista.insertar_al_inicio(9)
lista.insertar_al_inicio(30)
lista.mostrar_desde_inicio()  # Salida: 0 1 2
lista.eliminar_del_final()
lista.mostrar_desde_inicio()  # Salida: 0 1 2

x = 22
# Búsqueda de un nodo
nodo = lista.buscar(x)
if nodo:
    print("Nodo encontrado:", x )  # Salida: Nodo encontrado: 1
else:
    print("Nodo no encontrado")