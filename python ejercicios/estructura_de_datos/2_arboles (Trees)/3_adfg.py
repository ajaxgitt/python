


# izquierda =  left
# derecha = right


class Nodo:
    def __init__(self, value) -> None:
        self.value = value 
        self.left = None
        self.right = None


class ArbolBinarioBusqueda:
    def __init__(self) -> None:
        self.root = None
    
    def insertar(self, dato):
        if self.root is None:
            self.root = Nodo(dato)
        else:
            self._insertar(self.root, dato)

    def _insertar(self, nodo, dato):
        if dato < nodo.value:
            if nodo.left is None:
                nodo.left = Nodo(dato)
            else:
                self._insertar(nodo.left, dato)
        else:
            if nodo.right is None:
                nodo.right = Nodo(dato)
            else:
                self._insertar(nodo.right, dato)
                
    def recorrido_inorden(self):
        self._recorrido_inorden(self.root)     

    def _recorrido_inorden(self,nodo):
        if nodo:
            self._recorrido_inorden(nodo.left)
            print(nodo.value)
            self._recorrido_inorden(nodo.right)

    def eliminar(self, nodo):
        self._eliminar(self.root, nodo)

    def _eliminar(self,raiz , nodo):
        if raiz is None:
            return None
        elif nodo < raiz.value:
            raiz.left = self._eliminar(raiz.left, nodo)
        elif nodo > raiz.value:
            raiz.right = self._eliminar(raiz.right, nodo)
        else:
            if raiz.left is None:
                return raiz.right
            if raiz.right is None:
                return raiz.left
            raiz.value = self._buscar_menor(raiz.right).value
            raiz.right = self._eliminar(raiz.right, raiz.value)
        return raiz
    
                
    def _buscar_menor(self, nodo):
        puntero = nodo
        while puntero.left:
            puntero = puntero.left 
        return puntero




# Uso del árbol
arbol = ArbolBinarioBusqueda()
arbol.insertar(34)
arbol.insertar(18)
arbol.insertar(72)
arbol.insertar(23)
arbol.insertar(5)
arbol.insertar(1)

print('-------------recorrido inorden')
arbol.recorrido_inorden()
arbol.eliminar(34)
print('-------------recorrido postorden')
arbol.recorrido_inorden()

# arbol.recorrido_postorden()