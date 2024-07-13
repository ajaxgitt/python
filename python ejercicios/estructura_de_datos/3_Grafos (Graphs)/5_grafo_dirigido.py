


class Nodo:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        

class Enlace:
    def __init__(self,origen,destino) -> None:
        self.origen = origen
        self.destino = destino
        
    def obtener_origen(self):
        return self.origen
    
    def obtener_destino(self):
        return self.destino   
        

class GrafoDirigido:
    def __init__(self) -> None:
        self.grafo = {}
        
    def insertar_nodo(self, nodo):
        if nodo in self.grafo:
            return print(f'el nodo {nodo}  ya existe en el grafo')
        else:
            self.grafo[nodo]=[]
            
    def conectar_nodos(self, origen , destino):
        
        enlace = Enlace(origen,destino)
        ori = enlace.obtener_origen()
        des = enlace.obtener_destino()
        
        if origen not in self.grafo:
            raise ValueError(f'El nodo {origen} no existe en el grafo')
        if destino not in self.grafo:
            print(f'El nodo {destino} no existe en el grafo')
            return
        
        self.grafo[ori].append(des)
        
    def imprimir(self):
        for nodo,enlaces in self.grafo.items():
            print(f'Nodo: {nodo} ---> {enlaces}')
    
        


graph = GrafoDirigido()
graph.insertar_nodo(5)
graph.insertar_nodo(6)
graph.insertar_nodo(10)
graph.imprimir()
print('conexion nodos')
graph.conectar_nodos(10,5)
graph.conectar_nodos(10,6)
graph.conectar_nodos(6,10)
graph.conectar_nodos(5,6)
graph.conectar_nodos(5,99)
graph.imprimir()
