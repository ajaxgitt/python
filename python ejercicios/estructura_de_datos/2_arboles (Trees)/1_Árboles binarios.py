# Ejercicio: Implementación de un Árbol Binario
# Descripción:
# Debes implementar una clase para un árbol binario y realizar las operaciones básicas: inserción, búsqueda y recorridos (inorden, preorden, y postorden).

# Requisitos:
# Nodo del Árbol Binario:

# Implementa una clase Nodo que represente un nodo en el árbol binario. Esta clase debe tener 
# atributos para almacenar el valor del nodo y referencias a los nodos hijo izquierdo y derecho.
# Árbol Binario:

# Implementa una clase ArbolBinario que represente el árbol binario. 
# Esta clase debe tener un atributo para almacenar la raíz del árbol.
# Métodos:

# insertar(valor): Inserta un nuevo nodo con el valor dado en el árbol binario.
# buscar(valor): Busca un nodo con el valor dado en el árbol binario. Devuelve True si el nodo existe y False en caso contrario.
# recorrido_inorden(): Devuelve una lista con los valores de los nodos en un recorrido inorden.
# recorrido_preorden(): Devuelve una lista con los valores de los nodos en un recorrido preorden.
# recorrido_postorden(): Devuelve una lista con los valores de los nodos en un recorrido postorden.
# Pistas:
# Para la inserción, sigue las reglas de un árbol binario de búsqueda: inserta el valor en el subárbol izquierdo si es menor que el nodo actual, o en el subárbol derecho si es mayor.
# Para la búsqueda, sigue las mismas reglas que para la inserción.
# Para los recorridos, utiliza la recursividad para visitar los nodos en el orden adecuado.




class Nodo:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.izquierdo = None
        self.derecho = None 



class ArbolBinario:
    def __init__(self) -> None:
        self.raiz = None
        
    def insertar(self,valor):
        nuevo_nodo = Nodo(valor)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            pass
            

























# # Crear un nuevo árbol binario
# arbol = ArbolBinario()

# # Insertar valores en el árbol
# arbol.insertar(50)
# arbol.insertar(30)
# arbol.insertar(70)
# arbol.insertar(20)
# arbol.insertar(40)
# arbol.insertar(60)
# arbol.insertar(80)

# # Buscar valores en el árbol
# print(arbol.buscar(40))  # Debería devolver True
# print(arbol.buscar(25))  # Debería devolver False

# # Obtener los recorridos del árbol
# print(arbol.recorrido_inorden())  # Debería devolver [20, 30, 40, 50, 60, 70, 80]
# print(arbol.recorrido_preorden()) # Debería devolver [50, 30, 20, 40, 70, 60, 80]
# print(arbol.recorrido_postorden())# Debería devolver [20, 40, 30, 60, 80, 70, 50]
