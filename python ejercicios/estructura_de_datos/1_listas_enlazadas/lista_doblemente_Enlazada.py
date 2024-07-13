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
    def __init__(self, valor) -> None:
        self.valor = valor
        self.anterior = None
        self.siguiente = None
        
    def __str__(self) -> str:
        return str(self.valor)
        


class ListaDoblementeEnlazada:
    def __init__(self) -> None:
        self.primer_nodo = None
        self.ultimo_nodo = None
        
        
        
    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.primer_nodo is None:
            self.primer_nodo = self.ultimo_nodo = Nodo(dato)
            return
        else:
            nuevo_nodo.siguiente = self.primer_nodo
            self.primer_nodo.anterior = nuevo_nodo
            self.primer_nodo =  nuevo_nodo
            
            
    def mostrar_desde_inicio(self):
        puntero = self.primer_nodo
        while puntero:
            print(puntero.valor, end=' <-> ')
            puntero = puntero.siguiente
        print('fin')
        
    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.primer_nodo is None:
            self.primer_nodo = self.ultimo_nodo = Nodo(dato)
            return
        else:
            self.ultimo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.ultimo_nodo
            self.ultimo_nodo = nuevo_nodo
            
    
    

# Prueba de las operaciones
lista = ListaDoblementeEnlazada()
lista.insertar_al_inicio(1)
lista.insertar_al_final(8)
lista.insertar_al_inicio(2)
lista.insertar_al_inicio(3)
lista.insertar_al_inicio(4)
lista.mostrar_desde_inicio()  # Salida: 0 1 2
# lista.mostrar_desde_final()   # Salida: 2 1 0
# lista.eliminar_del_inicio()
# lista.mostrar_desde_inicio()  # Salida: 1 2
lista.insertar_al_final(8)
lista.insertar_al_final(66)

# lista.insertar_al_inicio(10)

# lista.mostrar_desde_inicio()  # Salida: 1 2
# lista.mostrar_desde_final()   # Salida: 2 1
# lista.eliminar_del_final()
lista.mostrar_desde_inicio()  # Salida: 1
# lista.mostrar_desde_final()   # Salida: 1
# x = 15
# # Búsqueda de un nodo
# nodo = lista.buscar(x)
# if nodo:
#     print("Nodo encontrado:", x )  # Salida: Nodo encontrado: 1
# else:
#     print("Nodo no encontrado")