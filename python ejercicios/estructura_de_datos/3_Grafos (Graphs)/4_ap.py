
    

class Nodo:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        
    def obtener_nombre(self):
        return self.nombre 
    
    def __str__(self) -> str:
        return self.nombre
        
class Enlace:
    def __init__(self,origen,destino) -> None:
        self.origen = origen
        self.destino = destino
        
    def obtener_origen(self):
        return self.origen
    
    def obtener_destino(self):
        return self.destino
    
    def __str__(self) -> str:
        return self.origen.obtener_nombre()+' ----> '+self.destino.obtener_nombre()

    
class GrafoDirigido:
    def __init__(self) -> None:
        self.grafo = {}
        
    def insertar(self, nodo):
        if nodo in self.grafo:
            return f'el nodo {nodo}  ya existe en el grafo'
        self.grafo[nodo]= []

    def conectar_nodos(self, enlace):
        origen = enlace.obtener_origen()
        destino = enlace.obtener_destino()
        
        if origen not in self.grafo:
            raise ValueError(f'El nodo {origen} no existe en el grafo')
        if destino not in self.grafo:
            raise ValueError(f'El nodo {destino} no existe en el grafo')
        
        self.grafo[origen].append(destino)
        
    def __str__(self) -> str:
        enlaces = ''
        for origen in self.grafo:
            for destino in self.grafo[origen]:
                enlaces += origen.obtener_nombre() + ' ----> '+ destino.obtener_nombre() + '\n'
        
        return enlaces
        
    def obtener_nodo(self, nombre_nodo):
        for i  in self.grafo:
            if nombre_nodo == i.obtener_nombre():
                return i
        print('El nodo no existe')
    
    

def construir_grafo(grafo):
    g = grafo()
    for i in ('s','a','b','c','d','e','f','g','h','i','j','k'):
        g.insertar(Nodo(i))
    
    g.conectar_nodos(Enlace(g.obtener_nodo('s'),g.obtener_nodo('a')))
    g.conectar_nodos(Enlace(g.obtener_nodo('s'),g.obtener_nodo('a')))
    g.conectar_nodos(Enlace(g.obtener_nodo('k'),g.obtener_nodo('i')))
    g.conectar_nodos(Enlace(g.obtener_nodo('s'),g.obtener_nodo('j')))
    
    return g

G1 = construir_grafo(GrafoDirigido)
print(G1)