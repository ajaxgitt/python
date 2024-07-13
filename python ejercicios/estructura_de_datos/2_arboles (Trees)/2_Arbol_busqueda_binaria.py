
# insertar
# buscar
# eliminar
# recorrido_inorden
# recorrido_postorden

class Nodo:
    def __init__(self,valor) -> None:
        self.valor = valor
        self.izquierda = None
        self.derecha = None

    def __str__(self) -> str:
        return str(self.valor)




class ArbolBinarioBusqueda:
    
    def __init__(self) -> None:
        self.root = None
        
    def insertar(self, dato):
        if self.root is None:
            self.root = Nodo(dato)
        else:
            self._insertar(self.root, dato)
        
    def _insertar(self, nodo_raiz , dato):
        if dato < nodo_raiz.valor:
            if nodo_raiz.izquierda is None:
                nodo_raiz.izquierda = Nodo(dato)
            else:
                self._insertar(nodo_raiz.izquierda, dato)
        else:
            if nodo_raiz.derecha is None:
                nodo_raiz.derecha = Nodo(dato)
            else:
                self._insertar(nodo_raiz.derecha, dato)
                
    def recorrido_inorden(self):
        self._recorrido_inorden(self.root)
        
    def _recorrido_inorden(self, nodo_raiz):
        if nodo_raiz:
            self._recorrido_inorden(nodo_raiz.izquierda)
            print(nodo_raiz.valor)
            self._recorrido_inorden(nodo_raiz.derecha)

    def recorrido_postorden(self):
        self._recorrido_postorden(self.root)
        
    def _recorrido_postorden(self, nodo_raiz):
        if nodo_raiz:
            self._recorrido_postorden(nodo_raiz.derecha)
            print(nodo_raiz.valor)
            self._recorrido_postorden(nodo_raiz.izquierda)


    def buscar(self, nodo):
        self._buscar(self.root, nodo)
        
    def _buscar(self,raiz, nodo):
        if raiz is None:
            print(f'el nodo {nodo} no se encuentra en el arbol')
            return
        if raiz.valor == nodo:
            print(f'nodo {nodo} encontrado!!')
            return 
        if nodo < raiz.valor:
            self._buscar(raiz.izquierda, nodo) 
            
        else:
            self._buscar(raiz.derecha, nodo)
            
            
    def eliminar(self, nodo):
        self.root = self._eliminar(self.root, nodo)
        
    
    def _eliminar(self, raiz , nodo):
        if raiz is None:
            return None
        elif nodo < raiz.valor:
            raiz.izquierda = self._eliminar(raiz.izquierda, nodo)
        elif nodo > raiz.valor:
            raiz.derecha = self._eliminar(raiz.derecha, nodo)
        else:
            if raiz.izquierda is None:
                print(f'Nodo {nodo} eliminado correctamente!!')
                return raiz.derecha
            if raiz.derecha is None:
                print(f'Nodo {nodo} eliminado correctamente!!')
                return raiz.izquierda
            
            raiz.valor = self._buscar_menor(raiz.derecha).valor
            raiz.derecha = self._eliminar(raiz.derecha, raiz.valor)
        return raiz
    
    def _buscar_menor(self, raiz):
        puntero = raiz
        while puntero.izquierda:
            puntero = puntero.izquierda
        return puntero 
            
            










        
        
        

arbol = ArbolBinarioBusqueda()
arbol.insertar(50)   
arbol.insertar(25)   
arbol.insertar(75)   
arbol.insertar(12)   
arbol.insertar(37)   
arbol.insertar(62)   
arbol.insertar(87)   
arbol.insertar(1)

print('-------------recorrido inorden')
arbol.recorrido_inorden()
arbol.eliminar(1)
print('-------------recorrido postorden')
arbol.recorrido_postorden()

arbol.buscar(37)

